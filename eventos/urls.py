from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'eventos'  # Namespace do app

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('adicionar/', views.adicionar_evento, name='adicionar_evento'),
    path('editar/<int:id>/', views.editar_evento, name='editar_evento'),
    path('excluir/<int:id>/', views.excluir_evento, name='excluir_evento'),
    path('detalhes/<int:id>/', views.detalhes_evento, name='detalhes_evento'),
]

# Apenas necessário se você estiver lidando com arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
