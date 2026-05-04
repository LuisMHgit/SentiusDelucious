# Delivery App - Sentius Delicious

## Descripción
Aplicación web desarrollada con Django que permite a los usuarios gestionar pedidos y reservas de mesas de forma sencilla.

## Tecnologías
- Python 3
- Django
- PostgreSQL
- Bootsrap 

## Requisitos
- Python 3

## Instalación
python -m pip install --upgrade pip
python -m pip install django psycopg2-binary
python-dotenv

## Ejecución

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

## Configuracion
DB_NAME=sentiusdelicious_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432

## Funcionalidades implementadas
- Login de usuario
- Crear pedidos
- Listar pedidos
- Editar pedidos
- Eliminar pedidos
- Buscador de pedidos
- Crear reserva
- Editar reserva
- Eliminar reserva
- Listar reservas

## Funcionalidades pendientes
- Mejora Visual
- Repartidor

##  Problemas conocidos
- Posibles errores si fechas no tienen formato correcto
- Formularios sin validación avanzada

## Autor
Luis - 2º DAM