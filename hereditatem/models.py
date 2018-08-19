# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Fragment(models.Model):
    front_scan = models.ImageField(upload_to = 'fragments_img/', null = False, blank = False)
    back_scan = models.ImageField(upload_to = 'fragments_img/', null = False, blank = False)
    width = models.FloatField(blank=True)
    height = models.FloatField(blank=True)
    thickness = models.FloatField(blank=True)
    creation_date = models.DateField(auto_now=True)   
