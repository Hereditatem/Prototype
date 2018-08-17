# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# Create your views here.

def index(request):
    return redirect('/hereditatem/panels')

def panels(request):
    context = {
        'page_title': "Tile Panels",
    }
    return render(request, 'index.html', context)

def fragments(request):
    context = {
        'page_title': "Fragments",
    }
    return render(request, 'fragments.html', context)

def fragment(request, fragment_id = None):
    pagetitle = "Fragment Details"
    if fragment_id == None :
        pagetitle = "Add Fragment"
    context = {
        'page_title': pagetitle,
    }
    return render(request, 'fragment.html', context)

