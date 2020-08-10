from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("a/",views.pre,name="pre"),
    path("delete/<str:id>/",views.delete,name="delete")
]
