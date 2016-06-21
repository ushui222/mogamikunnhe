from django.conf.urls import url

from . import views

app_name = 'umbrella_system'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /umbrella_system/date/20160601/
    url(r'^date/([0-9]+)/$', views.date, name='date'),
    url(r'^room/$', views.room, name='room'),
    url(r'^table/$', views.table, name='table'),
]