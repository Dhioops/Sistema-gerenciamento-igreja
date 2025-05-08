from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_escala, name='listar_escala'),  # será /escala/
    path('adicionar/', views.adicionar_escala, name='adicionar_escala'),
    path('editar/<int:pk>/', views.editar_escala, name='editar_escala'),
    path('excluir/<int:pk>/', views.excluir_escala, name='excluir_escala'),
    path('autocomplete/membros/', views.autocomplete_membros, name='autocomplete_membros'),
    path('buscar-membros/', views.buscar_membros, name='buscar_membros'),
]
