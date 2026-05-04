from django import forms
from .models import Reserva
from .models import Pedido

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['fecha_reserva', 'numero_personas', 'mesa_id', 'estado']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['producto', 'direccion']