from django.contrib import admin

from .models import QuickNote


class QuickNoteAdmin(admin.ModelAdmin):

    list_display = ['note', 'file', 'create_date', 'update_date']
    list_filter = ['create_date', 'update_date']
    search_fields = ('note',)


admin.site.register(QuickNote, QuickNoteAdmin)
