from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^reg/$', views.reg),
    url(r'^logout/$', views.logout),
    url(r'^appointments/$', views.appointments),
    url(r'^appointments/logout/$', views.logout),
    url(r'^appointments/add/(?P<id>\d+)$', views.add),
    url(r'^appointments/edit/(?P<id>\d+)$', views.edit),
    url(r'^appointments/add/addapt/$', views.addapt),
    url(r'^appointments/delete/(?P<id>\d+)$', views.delete),
    url(r'^appointments/edit/editprocess/(?P<id>\d+)$', views.editprocess),

]