from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^textbook/$', views.IndexView.as_view(), name="textbook"),
    #url(r'^chapter/$', views.chapter, name="chapter"),
]