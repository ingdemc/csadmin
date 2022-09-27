from django.urls import path
from cargasemantica.views import ConexionListView
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path(r'verconexion/', views.ConexionListView.as_view(), name='verconexion'),
    path(r'calificacion/', views.calificacion, name='calificacion'),
    path('crearconexion/', views.crearconexion, name='crearconexion'),
    path(r'dtabla/<str:id>/<int:ide>', views.detalle_tab, name='dtabla'),
    path(r'dashboard/', views.dashboard),
    path(r'recursividad/<int:ide>', views.recursividad, name='recursividad'),
    path(r'eliminacion/<int:id>', views.eliminacion, name='eliminacion'),
   
    ]