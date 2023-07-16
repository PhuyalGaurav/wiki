from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.entries, name="entries"),
    path("random/",views.random , name="random" ),
    path("search/", views.search, name="search"),
    path("create/", views.create, name="create"),
    path("error/", views.error, name="error"),
    path("edited/", views.edit, name="edit"),
    path("edit/", views.rledit2, name="rledit2"),
    path("delete/", views.delete, name="delete")
 ]
