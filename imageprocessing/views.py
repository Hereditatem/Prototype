# -*- coding: utf-8 -*-
from __future__ import unicode_literals


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
            # Processor.segment(dataFile)

            return HttpResponse("You're at the Segment Mehtod. This is your data: ")
        # except:
            # e = sys.exc_info()[0]
            # return HttpResponse("We've got a proglem")
            
