from django.urls import path

from .views import (soportes)
urlpatterns = [
    path(r'soportes/', soportes, name = "soportes"),
    ]