from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(status='active')


class Action(models.Model):

    ACTION_STATUS = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )

    title = models.CharField(max_length=512, null=False, blank=False)
    slug = models.SlugField(max_length=512)
    author = models.ForeignKey(User, related_name='actions')
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=ACTION_STATUS, default='active')

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('sportlife: action_detail', args=[self.title])

    objects = models.Manager()
    active = ActiveManager()

