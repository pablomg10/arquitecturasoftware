from django.urls import path
from .views import (
    lista_clientes, detalle_cliente,
    lista_coches, lista_servicios,
    registrar_cliente, registrar_coche, registrar_servicio,
    buscar_cliente, buscar_coche_por_matricula,
    buscar_coches_de_cliente, buscar_servicios_de_coche,
    nuevo_cliente, nuevo_coche, nuevo_servicio, nuevo_coche_servicio,
    inicio, acerca_de, contacto
)

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('acerca/', acerca_de, name='acerca'),
    path('contacto/', contacto, name='contacto'),

    path('clientes/', lista_clientes, name='lista_clientes'),
    path('coches/', lista_coches, name='lista_coches'),
    path('servicios/', lista_servicios, name='lista_servicios'),

    # URLs originales
    path('clientes/<int:cliente_id>/', detalle_cliente, name='detalle_cliente'),
    path('clientes/nuevo/', nuevo_cliente, name='nuevo_cliente'),
    path('coches/nuevo/', nuevo_coche, name='nuevo_coche'),
    path('servicios/nuevo/', nuevo_servicio, name='nuevo_servicio'),
    path('coche-servicio/nuevo/', nuevo_coche_servicio, name='nuevo_coche_servicio'),
    
    # URLs para registro
    path('clientes/registrar/', registrar_cliente, name='registrar_cliente'),
    path('coches/registrar/', registrar_coche, name='registrar_coche'),
    path('servicios/registrar/', registrar_servicio, name='registrar_servicio'),
    
    # URLs para búsqueda
    path('buscar/clientes/<int:cliente_id>/', buscar_cliente, name='buscar_cliente'),
    path('buscar/coches/matricula/<str:matricula>/', buscar_coche_por_matricula, name='buscar_coche_por_matricula'),
    path('buscar/clientes/<int:cliente_id>/coches/', buscar_coches_de_cliente, name='buscar_coches_de_cliente'),
    path('coches/<int:coche_id>/servicios/', buscar_servicios_de_coche, name='buscar_servicios_de_coche'),
]