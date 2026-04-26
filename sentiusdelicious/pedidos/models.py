

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.producto} - {self.direccion} de {self.usuario}"
    
class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 
    mesa_id = models.IntegerField()  
    fecha_reserva = models.DateTimeField()  
    numero_personas = models.IntegerField() 

    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

    def __str__(self):
        return f"Reserva de {self.usuario} para {self.numero_personas} personas el {self.fecha_reserva}"