

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pedido

@login_required
def lista_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user)
    return render(request, 'lista.html', {'pedidos': pedidos})

@login_required
def crear_pedido(request):
    if request.method == 'POST':
        Pedido.objects.create(
            usuario=request.user,
            producto=request.POST['producto'],
            direccion=request.POST['direccion']
        )
        return redirect('/')
    return render(request, 'crear.html')