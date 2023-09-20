"""
URL configuration for mazer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from mazer import settings
from django.conf.urls.static import static

urlpatterns = [
    #rota, view responsavel, nome de referencia
    #facebook.com
        #path('')
    #facebook.com/thye
        #path('/thye')
    path('admin321/', admin.site.urls),
    #path usuarios
    path('', include('usuarios.urls')),
    #paths produtos
    path('produtos/', include('mazerapp.urls')),
]

handler404 = "usuarios.views.handler404"

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
