# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-07 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scan2D',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_image', models.ImageField(upload_to='fragments_img/')),
                ('segmented_image', models.ImageField(null=True, upload_to='fragments_img/')),
            ],
        ),
    ]