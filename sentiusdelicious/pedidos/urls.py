from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pedidos, name='lista_pedidos'),
    path('crear/', views.crear_pedido, name='crear_pedido'),
    path('editar/<int:pedido_id>/', views.editar_pedido, name='editar_pedido'),
    path('eliminar/<int:pedido_id>/', views.eliminar_pedido, name='eliminar_pedido'),
    path('reservas/', views.lista_reservas, name='lista_reservas'),
    path('reservas/crear/', views.crear_reserva, name='crear_reserva'),
    path('reservas/editar/<int:reserva_id>/', views.editar_reserva, name='editar_reserva'),
    path('reservas/eliminar/<int:reserva_id>/', views.eliminar_reserva, name='eliminar_reserva'),
]