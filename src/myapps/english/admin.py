# -*- coding: utf-8 -*-


from django.contrib import admin
from .models import Words


class WordsAdmin(admin.ModelAdmin):

    list_display = ['word', 'translation', 'comment']
    list_filter = ['word']


admin.site.register(Words, WordsAdmin)
