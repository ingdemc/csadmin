from django.urls import path
from cargasemantica.views import ConexionListView
from . import views
from .views import (
    eliminacion,calificacion,recursividad
)
urlpatterns = [
    path(r'verconexion/', ConexionListView.as_view(), name='ver_conexion'),
    path('index', views.index, name='index'),
    path(r'calificacion/', calificacion, name='calificacion'),
    path('crearconexion/', views.crearconexion, name='crearconexion'),
    path(r'dashboard/', views.dashboard),
    path(r'recursividad/<str:view>/<int:id>', recursividad, name='eliminacion'),
    path(r'schema/<int:id>', views.schema, name='schema'),
    path(r'reglas/<int:id>', views.reglas, name='reglas'),
    path(r'tablas/<int:id>', views.tablas, name='tablas'),
    path(r'comentarios/<int:id>', views.comentarios, name='comentarios'),
    path(r'eliminacion/<int:id>', eliminacion, name='eliminacion'),
    ]