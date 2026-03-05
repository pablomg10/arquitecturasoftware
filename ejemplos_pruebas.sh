# Ejemplos de pruebas para los endpoints del taller de coches
# Ejecutar estos comandos desde la terminal o usar Postman

## 1. REGISTRAR CLIENTE
curl -X POST http://127.0.0.1:8000/gestion/clientes/registrar/ \
    -H "Content-Type: application/json" \
    -d '{"nombre": "Juan Pérez", "telefono": "666123456", "email": "juan.perez@email.com"}'

curl -X POST http://127.0.0.1:8000/gestion/clientes/registrar/ \
    -H "Content-Type: application/json" \
    -d '{"nombre": "María García", "telefono": "677234567", "email": "maria.garcia@email.com"}'

## 2. REGISTRAR COCHE
curl -X POST http://127.0.0.1:8000/gestion/coches/registrar/ \
    -H "Content-Type: application/json" \
    -d '{"cliente_id": 1, "marca": "Toyota", "modelo": "Corolla", "matricula": "1234ABC"}'

curl -X POST http://127.0.0.1:8000/gestion/coches/registrar/ \
    -H "Content-Type: application/json" \
    -d '{"cliente_id": 1, "marca": "Honda", "modelo": "Civic", "matricula": "5678DEF"}'

curl -X POST http://127.0.0.1:8000/gestion/coches/registrar/ \
    -H "Content-Type: application/json" \
    -d '{"cliente_id": 2, "marca": "Ford", "modelo": "Focus", "matricula": "9012GHI"}'

## 3. REGISTRAR SERVICIO
curl -X POST http://127.0.0.1:8000/gestion/servicios/registrar/ \
    -H "Content-Type: application/json" \
    -d '{"coche_id": 1, "nombre": "Cambio de aceite", "descripcion": "Cambio completo de aceite del motor"}'

curl -X POST http://127.0.0.1:8000/gestion/servicios/registrar/ \
    -H "Content-Type: application/json" \
    -d '{"coche_id": 1, "nombre": "Revisión de frenos", "descripcion": "Inspección completa del sistema de frenos"}'

curl -X POST http://127.0.0.1:8000/gestion/servicios/registrar/ \
    -H "Content-Type: application/json" \
    -d '{"coche_id": 2, "nombre": "Cambio de neumáticos", "descripcion": "Sustitución de neumáticos gastados"}'

## 4. BÚSQUEDAS
# Buscar cliente por ID
curl -X GET http://127.0.0.1:8000/gestion/buscar/clientes/1/

# Buscar coche por matrícula
curl -X GET http://127.0.0.1:8000/gestion/buscar/coches/matricula/1234ABC/

# Buscar todos los coches de un cliente
curl -X GET http://127.0.0.1:8000/gestion/buscar/clientes/1/coches/

# Buscar todos los servicios de un coche
curl -X GET http://127.0.0.1:8000/gestion/buscar/coches/1/servicios/

## URLs disponibles:
# POST http://127.0.0.1:8000/gestion/clientes/registrar/
# POST http://127.0.0.1:8000/gestion/coches/registrar/
# POST http://127.0.0.1:8000/gestion/servicios/registrar/
# GET  http://127.0.0.1:8000/gestion/buscar/clientes/<id>/
# GET  http://127.0.0.1:8000/gestion/buscar/coches/matricula/<matricula>/
# GET  http://127.0.0.1:8000/gestion/buscar/clientes/<id>/coches/
# GET  http://127.0.0.1:8000/gestion/buscar/coches/<id>/servicios/