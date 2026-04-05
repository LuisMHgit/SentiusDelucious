# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pedido


@login_required
def lista_pedidos(request):
    """
    Muestra la lista de pedidos del usuario autenticado.
    Permite filtrar por nombre de producto usando un parámetro GET (?q=...).
    """
    query = request.GET.get('q')

    # Filtrar pedidos del usuario actual
    pedidos = Pedido.objects.filter(usuario=request.user)

    # Aplicar búsqueda si existe query
    if query:
        pedidos = pedidos.filter(producto__icontains=query)

    return render(request, 'lista.html', {'pedidos': pedidos})


@login_required
def crear_pedido(request):
    """
    Crea un nuevo pedido asociado al usuario autenticado.
    """
    if request.method == 'POST':
        # Crear pedido con datos del formulario
        Pedido.objects.create(
            usuario=request.user,
            producto=request.POST.get('producto'),
            direccion=request.POST.get('direccion')
        )
        return redirect('lista_pedidos')  # Mejor usar nombre de ruta

    return render(request, 'crear.html')


@login_required
def editar_pedido(request, pedido_id):
    """
    Permite editar un pedido existente del usuario.
    Solo se puede acceder si el pedido pertenece al usuario autenticado.
    """
    pedido = get_object_or_404(
        Pedido,
        id=pedido_id,
        usuario=request.user  # Seguridad: evita acceder a pedidos de otros usuarios
    )

    if request.method == 'POST':
        # Actualizar campos del pedido
        pedido.producto = request.POST.get('producto')
        pedido.direccion = request.POST.get('direccion')
        pedido.save()

        return redirect('lista_pedidos')

    return render(request, 'editar.html', {'pedido': pedido})


@login_required
def eliminar_pedido(request, pedido_id):
    """
    Elimina un pedido del usuario autenticado.
    """
    pedido = get_object_or_404(
        Pedido,
        id=pedido_id,
        usuario=request.user
    )

    pedido.delete()
    return redirect('lista_pedidos')