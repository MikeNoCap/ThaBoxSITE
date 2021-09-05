from django.urls import path
from django.shortcuts import redirect
from. import views


# UrlConf
urlpatterns = [
    path("", lambda request: redirect("home/")),
    path("home/", views.home),
    path("contribute/", views.contribute),
    path("download/", views.download)
]