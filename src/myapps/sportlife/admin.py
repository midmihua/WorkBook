from django.contrib import admin
from .models import Action


class ActionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'updated', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {
        'slug': ('title',)
    }
    ordering = ['title', 'updated']
    raw_id_fields = ('author',)


admin.site.register(Action, ActionAdmin)
