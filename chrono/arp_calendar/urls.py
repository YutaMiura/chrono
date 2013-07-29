from django.conf.urls import patterns, url

from arp_calendar import views

urlpatterns = patterns('',
    url(r'^index/$', views.index, name="index!"),
    # url(r'^index2/$', views.index_by_shortcut, name="index!"),
    url(r'^list/(?P<year>\d{4})/(?P<month>\d{2})/$',
        views.list_calendar, name="listing calendar"),
)
