from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pedidos),
    path('crear/', views.crear_pedido),
    path('editar/<int:id>/', views.editar_pedido, name='editar_pedido'),
    path('eliminar/<int:id>/', views.eliminar_pedido, name='eliminar_pedido'),
]