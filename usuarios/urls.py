from django.urls import path
from . import views
from .views import (
    login_view,register
)
urlpatterns = [
    path(r'login/', login_view, name = "login"),
    path(r'register/', register, name="register"),
    ]