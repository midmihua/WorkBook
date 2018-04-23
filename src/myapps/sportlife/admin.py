# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Action, Day, DayList, Program, ProgramList


class ActionAdmin(admin.ModelAdmin):

    list_display = ['action', 'description', 'update_date']
    list_filter = ['action']
    search_fields = ('action', 'description')


class DayAdmin(admin.ModelAdmin):

    list_display = ['day', 'update_date']
    list_filter = ['day']
    search_fields = ('day',)


class DayListAdmin(admin.ModelAdmin):

    list_display = ['day', 'action', 'update_date']
    list_filter = ['day', 'action']
    search_fields = ('day', 'action')


class ProgramAdmin(admin.ModelAdmin):

    list_display = ['program', 'description', 'update_date']
    list_filter = ['program']
    search_fields = ('program', 'description')


class ProgramListAdmin(admin.ModelAdmin):

    list_display = ['program', 'day', 'level', 'update_date']
    list_filter = ['program', 'day']
    search_fields = ('program', 'day')


admin.site.register(Action, ActionAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(DayList, DayListAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(ProgramList, ProgramListAdmin)
