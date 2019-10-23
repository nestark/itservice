from django.urls import path,re_path, include
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^topics/$', views.topics, name='topics'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    re_path(r'^search/$', views.search, name='search'),

]