# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import TCUser, TCUserMedia


class TCUserAdmin(admin.ModelAdmin):

    list_display = ['username', 'token', 'update_date']
    list_filter = ['username']
    search_fields = ('username',)


class TCUserMediaAdmin(admin.ModelAdmin):

    list_display = ['username', 'media', 'update_date']
    list_filter = ['username']
    search_fields = ('username', 'media')


admin.site.register(TCUser, TCUserAdmin)
admin.site.register(TCUserMedia, TCUserMediaAdmin)