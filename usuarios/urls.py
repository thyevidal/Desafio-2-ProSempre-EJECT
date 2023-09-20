from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth-register', views.cadastrarUser, name='auth-register'),
    path('editar-usuario', views.editarUsuario, name='editar-usuario'),
    path('logout', views.logout, name='logout'),
]