# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Market, Pair, Stat


class MarketAdmin(admin.ModelAdmin):

    list_display = ['market', 'url']
    list_filter = ['market',]
    search_fields = ('market',)


class PairAdmin(admin.ModelAdmin):

    list_display = ['pair', 'description']
    list_filter = ['pair',]
    search_fields = ('pair',)


class StatAdmin(admin.ModelAdmin):

    list_display = ['market', 'pair', 'interval']
    list_filter = ['market', 'pair']
    search_fields = ('market', 'pair')


admin.site.register(Market, MarketAdmin)
admin.site.register(Pair, PairAdmin)
admin.site.register(Stat, StatAdmin)
