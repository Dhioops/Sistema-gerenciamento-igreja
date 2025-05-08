from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_membros, name='lista_membros'),
    path('adicionar/', views.adicionar_membro, name='adicionar_membro'),
    path('editar/<int:id>/', views.editar_membro, name='editar_membro'),
    path('excluir/<int:id>/', views.excluir_membro, name='excluir_membro'),
]
