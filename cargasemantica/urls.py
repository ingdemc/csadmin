from django.urls import path
from cargasemantica.views import ConexionListView
from . import views
from .views import (
    login_view, eliminacion, soportes,calificacion
)
urlpatterns = [
    
    path(r'verconexion/', ConexionListView.as_view(), name='ver_conexion'),
    #  path(r'metadatos/<int:id>', metadatos.as_view(), name='metadatos'),
    # path(r'metadatos/schema/', metadatos.schema, name='metadatos'),
    path('index', views.index, name='index'),
    path(r'calificacion/', calificacion, name='calificacion'),
    # path(r'login/', views.login, name='login'),
    path(r'register/', views.register, name='registro'),
    # path(r'verconexiones/', views.verconexiones),
    path('crearconexion/', views.crearconexion, name='crearconexion'),
    path(r'dashboard/', views.dashboard),
    # path(r'metadatos/', views.metadatos, name='metadatos'),
    path(r'schema/<int:id>', views.schema, name='schema'),
    path(r'reglas/', views.reglas, name='reglas'),
    path(r'tablas/', views.tablas, name='tablas'),
    path(r'login/', login_view, name = "login"),
    path(r'soportes/', soportes, name = "soportes"),
    path(r'comentarios/', views.comentarios, name='comentarios'),
    # path('eliminacion/<int:id>', eliminacion),
    path(r'eliminacion/<int:id>', eliminacion, name='eliminacion'),
    ]