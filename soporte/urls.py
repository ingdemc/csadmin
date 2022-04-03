from django.urls import path
from cargasemantica.views import ConexionListView
from . import views
from .views import (soportes)
urlpatterns = [
    path(r'soportes/', soportes, name = "soportes"),
    ]