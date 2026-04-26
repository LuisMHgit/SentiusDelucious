from django.contrib import admin
from .models import Pedido
from .models import Reserva

admin.site.register(Pedido)
admin.site.register(Reserva)