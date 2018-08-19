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
                front_scan = form.cleaned_data["frontscan"]
                back_scan = form.cleaned_data["backscan"]
                fragment = Fragment(width=width, height=height, thickness=thickness,
                                    front_scan=front_scan, back_scan=back_scan)
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
