from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.entries, name="entries"),
    path("random/",views.random , name="random" ),
    path("search/", views.search, name="search")
 ]
