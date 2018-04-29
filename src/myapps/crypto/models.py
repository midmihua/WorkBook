# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.postgres.fields import JSONField


class Basic(models.Model):

    STATUS = (
        ('AC', 'A'),
        ('DC', 'D'),
    )

    description = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=STATUS, default='AC')

    class Meta:
        abstract = True


class Market(Basic):

    market = models.CharField(max_length=255, null=False, blank=False, unique=True)
    url = models.URLField(null=True, blank=True)
    market_status = JSONField(null=True, blank=True)

    class Meta:
        verbose_name = 'Market'
        verbose_name_plural = 'Markets'

    def __str__(self):
        return self.market

    def save(self, *args, **kwargs):
        self.market = self.market.lower()
        return super(Market, self).save(*args, **kwargs)


class Pair(Basic):

    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    pair = models.CharField(max_length=15, null=False, blank=False)

    class Meta:
        verbose_name = 'Pair'
        verbose_name_plural = 'Pairs'
        unique_together = (('market', 'pair'),)

    def get_market(self):
        return self.market

    def get_name(self):
        return self.pair

    def __str__(self):
        return '{0}: {1}'.format(self.market, self.pair)

    def save(self, *args, **kwargs):
        self.pair = self.pair.upper()
        return super(Pair, self).save(*args, **kwargs)


class Stat(Basic):

    INTERVAL = (
        ('KLINE_INTERVAL_1MINUTE', '1m'),
        ('KLINE_INTERVAL_3MINUTE', '3m'),
        ('KLINE_INTERVAL_5MINUTE', '5m'),
        ('KLINE_INTERVAL_15MINUTE', '15m'),
        ('KLINE_INTERVAL_30MINUTE', '30m'),
        ('KLINE_INTERVAL_1HOUR', '1h'),
        ('KLINE_INTERVAL_2HOUR', '2h'),
        ('KLINE_INTERVAL_4HOUR', '4h'),
    )

    PERIOD = (
        ('1H', '1 hour ago UTC'),
        ('2H', '2 hours ago UTC'),
        ('4H', '4 hours ago UTC'),
        ('6H', '6 hours ago UTC'),
        ('8H', '8 hours ago UTC'),
        ('12H', '12 hours ago UTC'),
        ('24H', '24 hours ago UTC'),
        ('36H', '36 hours ago UTC'),
        ('48H', '48 hours ago UTC'),
    )

    NOTIFICATION = (
        ('ON', 'ON'),
        ('OFF', 'OFF'),
    )

    interval = models.CharField(max_length=25, choices=INTERVAL, default='KLINE_INTERVAL_15MINUTE')
    period = models.CharField(max_length=100, choices=PERIOD, default='2H')
    pair = models.ForeignKey(Pair, on_delete=models.CASCADE)
    pair_info = JSONField(null=True, blank=True)
    market_depth = JSONField(null=True, blank=True)
    recent_trades = JSONField(null=True, blank=True)
    historical_candlesticks = JSONField(null=True, blank=True)
    _24h_ticker = JSONField(null=True, blank=True)
    notification = models.CharField(max_length=3, choices=NOTIFICATION, default='OFF')

    def get_interval(self):
        return dict(Stat.INTERVAL)[str(self.interval)]

    def get_period(self):
        return dict(Stat.PERIOD)[str(self.period)]

    def get_notification(self):
        return dict(Stat.NOTIFICATION)[str(self.notification)]

    class Meta:
        verbose_name = 'Stat'
        verbose_name_plural = 'Stats'
