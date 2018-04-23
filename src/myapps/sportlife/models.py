# -*- coding: utf-8 -*-

from django.db import models


class Action(models.Model):

    action = models.CharField(max_length=256, blank=False, null=False, unique=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Action'
        verbose_name_plural = 'Actions'

    def __str__(self):
        return self.action


class Day(models.Model):

    day = models.CharField(max_length=50, null=False, blank=False, unique=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Day'
        verbose_name_plural = 'Day'

    def __str__(self):
        return self.day


class DayList(models.Model):

    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'DayList'
        verbose_name_plural = 'DayLists'

    def __str__(self):
        return self.day


class Program(models.Model):

    program = models.CharField(max_length=100, null=False, blank=False, unique=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Program'
        verbose_name_plural = 'Programs'

    def __str__(self):
        return self.program


class ProgramList(models.Model):

    variant = (
        ('HA', 'Hard'),
        ('ME', 'Medium'),
        ('LI', 'Light')
    )

    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    level = models.CharField(max_length=2, choices=variant, default='ME')
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'ProgramList'
        verbose_name_plural = 'ProgramLists'

    def __str__(self):
        return self.program + '_' + self.day


class Execution(models.Model):

    pass
