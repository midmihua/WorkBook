# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Market, Pair, Stat


class MarketAdmin(admin.ModelAdmin):

    list_display = ['market', 'url', 'status', 'update_date']
    list_filter = ['market']
    search_fields = ('market',)


class PairAdmin(admin.ModelAdmin):

    list_display = ['market', 'pair', 'status', 'update_date']
    list_filter = ['market', 'pair']
    search_fields = ('market', 'pair')


class StatAdmin(admin.ModelAdmin):

    list_display = ['pair', 'interval', 'period', 'notification', 'status', 'update_date']
    list_filter = ['pair']
    list_editable = ('interval', 'period', 'status', 'notification')
    search_fields = ('pair',)


admin.site.register(Market, MarketAdmin)
admin.site.register(Pair, PairAdmin)
admin.site.register(Stat, StatAdmin)
