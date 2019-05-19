# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField


class VideoFragment(models.Model):

    filename = models.CharField(max_length=255)
    details = JSONField()

    def __str__(self):
        return '<Video File: {}>'.format(filename)

