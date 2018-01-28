from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.list_words, name='list_words'),
    url(r'^add/$', views.add_words, name='add_words'),
    url(r'^edit/(?P<word_id>[\w-]+)/$', views.edit_words, name='edit_words'),
    url(r'^delete/(?P<word_id>[\w-]+)/$', views.delete_words, name='delete_words'),
]
