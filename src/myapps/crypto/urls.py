from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.stat_view, name='stat_view'),
    url(r'^details/(?P<pair_id>[\w-]+)/$', views.details, name='details'),
    url(r'^edit/(?P<pair_id>[\w-]+)/$', views.edit, name='edit'),
]
