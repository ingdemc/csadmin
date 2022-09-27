from django.urls import path

from . import views
urlpatterns = [
    path(r'soportes/', views.soportes, name = "soportes"),
      path(r'pg/', views.pgprincipal, name="pg"),
    # path(r'logout/', logout_user, name="logout"),
    path('register/',views.RegistrarUsuario,name = 'register'), 
   
    
    ]