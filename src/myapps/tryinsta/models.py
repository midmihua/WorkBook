# -*- coding: utf-8 -*-


from django.db import models
from django.contrib.postgres.fields import JSONField


class TCUser(models.Model):

    username = models.CharField(max_length=255, unique=True, blank=False, null=False)
    token = models.CharField(max_length=255, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'TCUser'
        verbose_name_plural = 'TCUsers'

    def __str__(self):
        return self.username


class TCUserMedia(models.Model):

    username = models.ForeignKey(TCUser, on_delete=models.CASCADE)
    update_date = models.DateTimeField(auto_now=True)
    media_id = models.CharField(max_length=255, null=True, blank=True)
    media_tags = JSONField(null=True, blank=True)
    media = JSONField(null=True, blank=True)

    class Meta:
        verbose_name = 'TCUserMedia'
        verbose_name_plural = 'TCUserMedias'
        unique_together = (('username', 'media_id'),)

    def __str__(self):
        return self.username.__str__() + '#' + str(self.pk)
