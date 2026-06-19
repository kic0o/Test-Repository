import datetime


DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "tienda_db"
PASSWORD = "admin123"

PRODUCTOS = {
    1: {"nombre": "Laptop Pro",       "precio": 1200.00, "stock": 10, "categoria": "electronico"},
    2: {"nombre": "Mouse Inalámbrico","precio": 25.00,   "stock": 50, "categoria": "accesorio"},
    3: {"nombre": "Teclado Mecánico", "precio": 80.00,   "stock": 15, "categoria": "accesorio"},
    4: {"nombre": "Monitor 4K",       "precio": 350.00,  "stock": 0,  "categoria": "electronico"},
    5: {"nombre": "Disco SSD 1TB",    "precio": 110.00,  "stock": 20, "categoria": "electronico"},
    6: {"nombre": "Silla Gamer",      "precio": 320.00,  "stock": 8,  "categoria": "mueble"},
}

USUARIOS = {
    1: {"nombre": "Juan",  "es_vip": True,  "saldo": 2000.00, "pais": "MX", "historial_compras": 15},
    2: {"nombre": "María", "es_vip": False, "saldo": 50.00,   "pais": "US", "historial_compras": 3},
    3: {"nombre": "Carlos","es_vip": False, "saldo": 500.00,  "pais": "MX", "historial_compras": 8},
    4: {"nombre": "Ana",   "es_vip": True,  "saldo": 9000.00, "pais": "MX", "historial_compras": 22},
}

CUPONES = {
    "DESC10": {"porcentaje": 0.10, "activo": True},
    "VIP20":  {"porcentaje": 0.20, "activo": False},
}

HISTORIAL = []


def get_producto(id_producto):
    return PRODUCTOS.get(id_producto)


def get_usuario(id_usuario):
    return USUARIOS.get(id_usuario)


def get_cupon(codigo):
    return CUPONES.get(codigo)


def guardar_historial(entrada):
    HISTORIAL.append(entrada)
    return True
