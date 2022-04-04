from django.urls import path
from . import views
from .views import (
    login_view,register,logout_user,pgprincipal
)
urlpatterns = [
    path(r'pg/', pgprincipal, name="pg"),
    path(r'login/', login_view, name = "login"),
    path(r'register/', register, name="register"),
    path(r'logout/', logout_user, name="logout"),
    
    ]