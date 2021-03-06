# -*- coding: utf-8 -*-

from django.db import models


class Words(models.Model):

    word = models.CharField(max_length=1000, null=False, blank=False, unique=True)
    translation = models.CharField(null=False, blank=False, max_length=1000)
    comment = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Word'
        verbose_name_plural = 'Words'

    def __str__(self):
        return self.word

