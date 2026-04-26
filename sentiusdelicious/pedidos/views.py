# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from backend.pedidos.forms import ReservaForm
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

from .models import Reserva

@login_required
def lista_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user)
    return render(request, 'reservas/lista_reservas.html', {'reservas': reservas})


@login_required
def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            reserva.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm()

    return render(request, 'reservas/crear_reserva.html', {'form': form})


@login_required
def editar_reserva(request, reserva_id):
    reserva = get_object_or_404(
        Reserva,
        id=reserva_id,
        usuario=request.user
    )

    if request.method == 'POST':
        reserva.mesa_id = request.POST.get('mesa_id')
        reserva.fecha_reserva = request.POST.get('fecha_reserva')
        reserva.numero_personas = request.POST.get('numero_personas')
        reserva.estado = request.POST.get('estado')
        reserva.save()

        return redirect('lista_reservas')

    return render(request, 'reservas/editar_reserva.html', {'reserva': reserva})


@login_required
def eliminar_reserva(request, reserva_id):
    reserva = get_object_or_404(
        Reserva,
        id=reserva_id,
        usuario=request.user
    )
    reserva.delete()
    return redirect('lista_reservas')