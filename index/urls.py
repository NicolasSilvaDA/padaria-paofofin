from django.urls import path
from index import views


urlpatterns = [
    path('', views.index_view, name='index_page'),
    path('padarias/', views.padarias_view, name='padarias_page'),
    path('padarias/<int:padaria_id>/inscrever/', views.inscrever_padaria, name='inscrever_padaria_page'),
    path('fornadas/', views.fornadas_view, name='fornadas_page'),
    path('fornadas/cadastrar/', views.cadastrar_fornada, name='cadastrar_fornada_page'),
    path('notificacoes/', views.notificacoes_view, name='notificacoes_page'),
]
