from django.db import models


class QuickNote(models.Model):

    note = models.TextField(unique=True, null=False, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    file = models.FileField(null=True, blank=True, upload_to='documents/%Y/%m/%d/')

    class Meta:
        verbose_name = 'QuickNote'
        verbose_name_plural = 'QuickNotes'

    def __str__(self):
        return self.note
