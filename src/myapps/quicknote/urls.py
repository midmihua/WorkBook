from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.list_notes, name='list_notes'),
    url(r'^add/$', views.add_note, name='add_note'),
    url(r'^edit/(?P<note_id>[\w-]+)/$', views.edit_note, name='edit_note'),
    url(r'^delete/(?P<note_id>[\w-]+)/$', views.delete_note, name='delete_note'),
]
