# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the Image Processing index.")

@csrf_exempt
def segment(request):
    if request.method == "GET" :
        return HttpResponse("Send Some image to be processed")
    elif request.method == "POST" :
        # try:
            data = request.FILES["data"]
            dataFile = data.file
            data.open()
            array = np.frombuffer(dataFile.read(),dtype=np.uint8)
            img = cv.imdecode(array, cv.IMREAD_UNCHANGED)#cv.IMREAD_COLOR)
            # gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
            # ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
            # # noise removal
            # kernel = np.ones((3,3),np.uint8)
            # opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel, iterations = 2)
            # # sure background area
            # sure_bg = cv.dilate(opening,kernel,iterations=3)
            # # Finding sure foreground area
            # dist_transform = cv.distanceTransform(opening,cv.DIST_L2,3)
            # ret, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)
            # # Finding unknown region
            # sure_fg = np.uint8(sure_fg)
            # unknown = cv.subtract(sure_bg,sure_fg)
            # # Marker labelling
            # ret, markers = cv.connectedComponents(sure_fg)
            # # Add one to all labels so that sure background is not 0, but 1
            # markers = markers+1
            # # Now, mark the region of unknown with zero
            # markers[unknown==255] = 0
            # markers = cv.watershed(img,markers)
            # img[markers == -1] = [255,0,255]
            
            #img = cv.pyrDown(img)
            gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
            ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
            # noise removal
            kernel = np.ones((3,3),np.uint8)
            opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel, iterations = 2)
            
            
            # # find contours and get the external one
            image, contours, hier = cv.findContours(gray, cv.RETR_TREE,
                            cv.CHAIN_APPROX_SIMPLE)
            
            # # with each contour, draw boundingRect in green
            # # a minAreaRect in red and
            # # a minEnclosingCircle in blue
            # minx = float("inf")
            # miny = float("inf")
            # maxh = 0
            # maxw = 0
            # for c in contours:
            #     # get the bounding rect
            #     x, y, w, h = cv.boundingRect(c)
            #     if x < minx :
            #         minx = x
            #     if y < miny :
            #         miny = y
            #     if x+w > maxw :
            #         maxw = x+w
            #     if y+h > maxh :
            #         maxh = y+h
            #     # draw a green rectangle to visualize the bounding rect

            #     # # get the min area rect
            #     # rect = cv.minAreaRect(c)
            #     # box = cv.boxPoints(rect)
            #     # # convert all coordinates floating point values to int
            #     # box = np.int0(box)
            #     # # draw a red 'nghien' rectangle
            #     # cv.drawContours(img, [box], 0, (0, 0, 255))
            
            #     # # finally, get the min enclosing circle
            #     # (x, y), radius = cv.minEnclosingCircle(c)
            #     # # convert all values to int
            #     # center = (int(x), int(y))
            #     # radius = int(radius)
            #     # # and draw the circle in blue
            #     # img = cv.circle(img, center, radius, (255, 0, 0), 2)
            
            # cv.rectangle(img, (minx, miny), (maxw, maxh), (0, 255, 0), 2)
            
            for c in contours:
                # get the bounding rect
                x, y, w, h = cv.boundingRect(c)
                # draw a green rectangle to visualize the bounding rect
                cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
                # get the min area rect
                rect = cv.minAreaRect(c)
                box = cv.boxPoints(rect)
                # convert all coordinates floating point values to int
                box = np.int0(box)
                # draw a red 'nghien' rectangle
                cv.drawContours(img, [box], 0, (0, 0, 255))
            
                # finally, get the min enclosing circle
                (x, y), radius = cv.minEnclosingCircle(c)
                # convert all values to int
                center = (int(x), int(y))
                radius = int(radius)
                # and draw the circle in blue
                img = cv.circle(img, center, radius, (255, 0, 0), 2)
            
            print(len(contours))
            cv.drawContours(img, contours, -1, (255, 255, 0), 1)

            mask = np.zeros(img.shape[:2],np.uint8)

            bgdModel = np.zeros((1,65),np.float64)
            fgdModel = np.zeros((1,65),np.float64)

            # rect = (minx,miny,maxw - minx,maxh - miny)
            # cv.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv.GC_INIT_WITH_RECT)

            # mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
            # img = img*mask2[:,:,np.newaxis]

            # print(len(contours))
            cv.drawContours(img, contours, -1, (255, 255, 0), 1)
            # img[markers == -1] = [255,0,255]
            
            # cv.imwrite("dist_transform.png", dist_transform)
            # cv.imwrite("fg.png", sure_fg)
            cv.imwrite("thresh.png", thresh)
            cv.imwrite("opening.png", opening)
            cv.imwrite("teste.png", img)

            return HttpResponse("You're at the Segment Mehtod. This is your data: ")
        # except:
            # e = sys.exc_info()[0]
            # return HttpResponse("We've got a proglem")
            
