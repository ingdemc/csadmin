"""csadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import logging
from django.contrib import admin
from django.urls import include,path
from django.contrib.auth import views as auth_views

from django.conf import settings


from csadmin.settings import base
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('cargasemantica.urls')),
    path('', include ('soporte.urls')),
  
    
    path('accounts/', include('django.contrib.auth.urls')),
    

] + static(base.STATIC_URL,document_root=base.STATIC_ROOT)
urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)