from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('garagens/', views.listar_garagens, name='listar_garagens'),
    path('garagens/nova/', views.criar_garagem, name='criar_garagem'),
    path('garagens/<int:pk>/editar/', views.editar_garagem, name='editar_garagem'),
    path('garagens/<int:pk>/excluir/', views.excluir_garagem, name='excluir_garagem'),
]