from django.urls import path
from . import views

urlpatterns = [
    path('dashboard.html', views.dashboard, name='dashboard'),
    path('meus-produtos', views.meusProdutos, name='meus-produtos'),
    path('registrar-produtos', views.registrarProdutos, name='registrar-produtos'),
    path('<id>/editar-produto', views.editarProduto, name='editar-produto'),
    path('<id>/deletar-produto', views.deletarProduto, name='deletar-produto'),
]