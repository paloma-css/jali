from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_resenhas, name='lista_resenhas'),
    path('resenha/<int:pk>/', views.detalhe_resenha, name='detalhe_resenha'),
    path('resenha/nova/', views.nova_resenha, name='nova_resenha'),
    path('resenha/<int:pk>/editar/', views.editar_resenha, name='editar_resenha'),
]