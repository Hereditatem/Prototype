# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.utils import timezone
from forms import FragmentForm
from models import Fragment
import mimetypes
import os
import numpy as np
import cv2 as cv
import time
import os
from contextlib import closing
from matplotlib import pyplot as plt
from django.core.files.temp import NamedTemporaryFile
from django.core.files.uploadedfile import InMemoryUploadedFile

class FragmentListView(ListView):

    model = Fragment
    paginate_by = 100  # if pagination is desired
    template_name = 'fragments.html'
    def get_context_data(self, **kwargs):
        context = super(FragmentListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



def index(request):
    return redirect('/hereditatem/panels')


def panels(request):
    context = {
        'page_title': "Tile Panels",
    }
    return render(request, 'index.html', context)


# def fragments(request):
#     context = {
#         'page_title': "Fragments",
#         'fragments': Fragment.}
#     return render(request, 'fragments.html', context)


def fragment(request, fragment_id=None):
    pagetitle = "Fragment Details: " + fragment_id
    fragment = None
    if request.method == 'GET':
        if fragment_id == None or fragment_id == '':
            pagetitle = "Add Fragment"
        else:
            fragment = Fragment.objects.get(pk=fragment_id)
    else:
        form = FragmentForm(request.POST,  request.FILES)
        if form.is_valid():
            width = form.cleaned_data["width"]
            height = form.cleaned_data["height"]
            thickness = form.cleaned_data["thickness"]
            if fragment_id == None or fragment_id == '':
                original_front_scan = form.cleaned_data["frontscan"]
                original_back_scan = form.cleaned_data["backscan"]
                front_scan = segment_tempfile(original_front_scan)
                back_scan = segment_tempfile(original_back_scan)
                fragment = Fragment(width=width, height=height, thickness=thickness,
                                    front_scan=front_scan, back_scan=back_scan,
                                    original_front_scan = original_front_scan, original_back_scan = original_back_scan)
                
            else:
                fragment = Fragment.objects.get(pk=fragment_id)
                fragment.thickness = thickness
                fragment.width = width
                fragment.height = height
            fragment.save()
    context = {
        'fragment': fragment,
        'page_title': pagetitle,
    }
    return render(request, 'fragment.html', context)

def segment_tempfile(tempfile):
    img = None
    if type(tempfile) is InMemoryUploadedFile :
        dataFile = tempfile.file
        tempfile.open()
        array = np.frombuffer(dataFile.read(),dtype=np.uint8)
        img = cv.imdecode(array, cv.IMREAD_UNCHANGED)
    else :
        img = cv.imread(tempfile.file.name)
    return segment(img)

def segment(img):
    ts = int(time.time())
    filename = 'tmp/%d.png' % ts
    cv.imwrite("debug/%d.png" % ts, img)
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    minx = float("inf")
    miny = float("inf")
    maxh = 0
    maxw = 0
    ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    # noise removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel, iterations = 2)

    image, contours, hier = cv.findContours(opening, cv.RETR_TREE,
                            cv.CHAIN_APPROX_SIMPLE)
    for c in contours:
        # get the bounding rect
        x, y, w, h = cv.boundingRect(c)
        if x < minx and x > 0:
            minx = x
        if y < miny and y > 0:
            miny = y
        if x+w > maxw :
            maxw = x+w
        if y+h > maxh :
            maxh = y+h
    
    print(len(contours))
    cv.drawContours(img, contours, -1, (255, 255, 0), 1)

    if minx == 0:
        minx = 5
    if miny == 0:
        miny = 5
    rect = (minx,miny,maxw - minx,maxh - miny)
    mask = np.zeros(img.shape[:2],np.uint8)
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    # rect = (50,50,450,290)
    cv.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img = img*mask2[:,:,np.newaxis]

    # mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    # img = img*mask2[:,:,np.newaxis]

    # print(len(contours))
    # cv.drawContours(img, contours, -1, (255, 255, 0), 1)
    # img[markers == -1] = [255,0,255]
            
    # cv.imwrite("debug/thresh_%d.png" % ts, thresh)
    # cv.imwrite("debug/opening:%d.png" % ts, opening)
    cv.imwrite(filename, img)
    
    data_file = NamedTemporaryFile()
    file = os.open(filename,os.O_RDONLY)
    try :
        for chunk in file.chunks() :
            data_file.write(chunk)
    finally:
        file.close()
    data_file.flush()


    return data_file


