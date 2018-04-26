# -*- coding: utf-8 -*-

from django.db import models


class Basic(models.Model):

    description = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Market(Basic):

    market = models.CharField(max_length=255, null=False, blank=False, unique=True)
    url = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = 'Market'
        verbose_name_plural = 'Markets'

    def __str__(self):
        return self.market


class Pair(Basic):

    pair = models.CharField(max_length=15, unique=True, null=False, blank=False)

    class Meta:
        verbose_name = 'Pair'
        verbose_name_plural = 'Pairs'

    def __str__(self):
        return self.pair


class Stat(Basic):

    VARIANTS = (
        ('KLINE_INTERVAL_1MINUTE', '1m'),
        ('KLINE_INTERVAL_3MINUTE', '3m'),
        ('KLINE_INTERVAL_5MINUTE', '5m'),
        ('KLINE_INTERVAL_15MINUTE', '15m'),
        ('KLINE_INTERVAL_30MINUTE', '30m'),
        ('KLINE_INTERVAL_1HOUR', '1h'),
        ('KLINE_INTERVAL_2HOUR', '2h'),
        ('KLINE_INTERVAL_4HOUR', '4h'),
        ('KLINE_INTERVAL_6HOUR', '6h'),
        ('KLINE_INTERVAL_8HOUR', '8h'),
        ('KLINE_INTERVAL_12HOUR', '12h'),
        ('KLINE_INTERVAL_1DAY', '1d'),
        ('KLINE_INTERVAL_3DAY', '3d'),
        ('KLINE_INTERVAL_1WEEK', '1w'),
        ('KLINE_INTERVAL_1MONTH', '1M'),
    )

    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    pair = models.ForeignKey(Pair, on_delete=models.CASCADE)
    interval = models.CharField(max_length=25, choices=VARIANTS, default='KLINE_INTERVAL_5MINUTE')

    def get_interval(self):
        return dict(Stat.VARIANTS)[str(self.interval)]

    class Meta:
        verbose_name = 'Stat'
        verbose_name_plural = 'Stats'
        unique_together = (('market', 'pair'),)

    def __str__(self):
        return '{0}:: {1}'.format(self.market, self.pair)


