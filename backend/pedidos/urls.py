from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pedidos),
    path('crear/', views.crear_pedido),
]