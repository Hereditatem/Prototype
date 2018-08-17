# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)


class Scan2D(models.Model):
    raw_image = models.ImageField(upload_to = 'fragments_img/', null = False, blank = False)
    segmented_image = models.ImageField(upload_to = 'fragments_img/', null = True)

class Fragment(models.Model):
    front_scan = models.OneToOneField(Scan2D,on_delete=models.CASCADE,related_name='+')
    back_scan = models.OneToOneField(Scan2D,on_delete=models.CASCADE,related_name='+')
    width = models.FloatField(blank=True)
    height = models.FloatField(blank=True)
    thickness = models.FloatField(blank=True)
    creation_date = models.DateField(auto_now=True)    
