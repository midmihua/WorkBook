# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Market, Pair, Stat, Rule, RuleMap, Notification, Messenger


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


class RuleAdmin(admin.ModelAdmin):

    list_display = ['rule', 'status', 'update_date']
    list_filter = ['rule']
    search_fields = ('rule',)


class RuleMapAdmin(admin.ModelAdmin):

    list_display = ['stat', 'rule', 'status', 'update_date', 'result']
    list_filter = ['stat', 'rule']
    search_fields = ('stat', 'rule')


class MessengerAdmin(admin.ModelAdmin):

    list_display = ['messenger', 'status', 'update_date']
    list_filter = ['messenger']
    search_fields = ('messenger',)


class NotificationAdmin(admin.ModelAdmin):

    list_display = ['rule', 'send_to', 'condition', 'status']
    list_filter = ['rule', 'send_to']
    search_fields = ('rule',)
    list_editable = ['condition', 'status']


admin.site.register(Market, MarketAdmin)
admin.site.register(Pair, PairAdmin)
admin.site.register(Stat, StatAdmin)
admin.site.register(Rule, RuleAdmin)
admin.site.register(RuleMap, RuleMapAdmin)
admin.site.register(Messenger, MessengerAdmin)
admin.site.register(Notification, NotificationAdmin)
