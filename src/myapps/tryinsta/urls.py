from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.users, name='users'),
    url(r'^media/(?P<tc_user_id>[\w-]+)/$', views.user_media, name='user_media'),
]
