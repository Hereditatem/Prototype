# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Scan2D, Fragment

# Register your models here.
admin.site.register(Scan2D)
admin.site.register(Fragment)
