from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^chapter/$', views.IndexView.as_view(), name="chapter"),
    #url(r'^chapter/$', views.chapter, name="chapter"),
]