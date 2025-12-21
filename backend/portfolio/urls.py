from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cases/", views.cases, name="cases"),
    path("investigations/", views.investigations, name="investigations"),
]
