from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Cliente, Coche, Servicio, CocheServicio
from .forms import ClienteForm, CocheForm, ServicioForm, CocheServicioForm, ContactoForm

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'app_gestion_coches/lista_clientes.html', {'clientes': clientes})

def lista_coches(request):
    coches = Coche.objects.all()
    return render(request, 'app_gestion_coches/lista_coches.html', {'coches': coches})

def lista_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'app_gestion_coches/lista_servicios.html', {'servicios': servicios})

def detalle_cliente(request, cliente_id):
    try:
        cliente = Cliente.objects.get(id=cliente_id)
        coches = Coche.objects.filter(cliente=cliente)
        context = {
            'cliente': cliente,
            'coches': coches
        }
        return render(request, 'app_gestion_coches/detalle_cliente.html', context)
    except Cliente.DoesNotExist:
        return JsonResponse({"error": "Cliente no encontrado"}, status=404)

# Nuevas funciones de registro
@csrf_exempt
def registrar_cliente(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cliente = Cliente.objects.create(
                nombre=data['nombre'],
                telefono=data['telefono'],
                email=data['email']
            )
            return JsonResponse({"mensaje": "Cliente registrado con éxito", "cliente_id": cliente.id})
        except KeyError:
            return JsonResponse({"error": "Datos incompletos"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def registrar_coche(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cliente = Cliente.objects.get(id=data['cliente_id'])
            coche = Coche.objects.create(
                cliente=cliente,
                marca=data['marca'],
                modelo=data['modelo'],
                matricula=data['matricula']
            )
            return JsonResponse({"mensaje": "Coche registrado con éxito", "coche_id": coche.id})
        except Cliente.DoesNotExist:
            return JsonResponse({"error": "Cliente no encontrado"}, status=404)
        except KeyError:
            return JsonResponse({"error": "Datos incompletos"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def registrar_servicio(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            coche = Coche.objects.get(id=data['coche_id'])
            servicio = Servicio.objects.create(
                nombre=data['nombre'],
                descripcion=data['descripcion']
            )
            CocheServicio.objects.create(coche=coche, servicio=servicio)
            return JsonResponse({"mensaje": "Servicio registrado con éxito", "servicio_id": servicio.id})
        except Coche.DoesNotExist:
            return JsonResponse({"error": "Coche no encontrado"}, status=404)
        except KeyError:
            return JsonResponse({"error": "Datos incompletos"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

# Nuevas funciones de búsqueda
@csrf_exempt
def buscar_cliente(request, cliente_id):
    try:
        cliente = Cliente.objects.values("id", "nombre", "telefono", "email").get(id=cliente_id)
        return JsonResponse(cliente)
    except Cliente.DoesNotExist:
        return JsonResponse({"error": "Cliente no encontrado"}, status=404)

@csrf_exempt
def buscar_coche_por_matricula(request, matricula):
    try:
        coche = Coche.objects.select_related('cliente').get(matricula=matricula)
        respuesta = {
            "coche": {
                "id": coche.id,
                "marca": coche.marca,
                "modelo": coche.modelo,
                "matricula": coche.matricula,
            },
            "cliente": {
                "id": coche.cliente.id,
                "nombre": coche.cliente.nombre,
                "telefono": coche.cliente.telefono,
                "email": coche.cliente.email,
            }
        }
        return JsonResponse(respuesta)
    except Coche.DoesNotExist:
        return JsonResponse({"error": "Coche no encontrado"}, status=404)

@csrf_exempt
def buscar_coches_de_cliente(request, cliente_id):
    try:
        coches = list(Coche.objects.filter(cliente_id=cliente_id).values("id", "marca", "modelo", "matricula"))
        return JsonResponse(coches, safe=False)
    except Cliente.DoesNotExist:
        return JsonResponse({"error": "Cliente no encontrado"}, status=404)

@csrf_exempt
def buscar_servicios_de_coche(request, coche_id):
    try:
        coche = Coche.objects.select_related('cliente').get(id=coche_id)
        coche_servicios = CocheServicio.objects.filter(coche=coche).select_related('servicio')
        context = {
            'coche': coche,
            'coche_servicios': coche_servicios
        }
        return render(request, 'app_gestion_coches/servicios_coche.html', context)
    except Coche.DoesNotExist:
        return JsonResponse({"error": "Coche no encontrado"}, status=404)


def nuevo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'app_gestion_coches/formulario.html', {'form': form, 'titulo': 'Nuevo Cliente'})


def nuevo_coche(request):
    if request.method == 'POST':
        form = CocheForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = CocheForm()
    return render(request, 'app_gestion_coches/formulario.html', {'form': form, 'titulo': 'Nuevo Coche'})


def nuevo_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ServicioForm()
    return render(request, 'app_gestion_coches/formulario.html', {'form': form, 'titulo': 'Nuevo Servicio'})


def nuevo_coche_servicio(request):
    if request.method == 'POST':
        form = CocheServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = CocheServicioForm()
    return render(request, 'app_gestion_coches/formulario.html', {'form': form, 'titulo': 'Nuevo CocheServicio'})

def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            return render(request, 'app_gestion_coches/gracias.html', {'nombre': nombre})
    else:
        formulario = ContactoForm()

    return render(request, 'app_gestion_coches/contacto.html', {'formulario': formulario})

def inicio(request):
    return render(request, 'app_gestion_coches/inicio.html')

def acerca_de(request):
    return render(request, 'app_gestion_coches/acerca.html')
