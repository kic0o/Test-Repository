import hashlib

import os
API_KEY = os.getenv('API_KEY')
DB_PASSWORD = os.getenv('DB_PASSWORD')
JWT_SECRET = os.getenv('JWT_SECRET')

import bcrypt

def hashear_password(password):
    # bcrypt genera una sal interna y produce un hash seguro
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed

def login(username, password):
    import sqlite3, bcrypt
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    # Consulta parametrizada para evitar inyección SQL
    query = "SELECT password FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    conn.close()
    # Verificar la contraseña usando bcrypt
    if result and bcrypt.checkpw(password.encode(), result[0]):
        return True
    return False

import jwt
import datetime

def generar_token(username, role):
    payload = {
        "sub": username,
        "role": role,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return token

def validar_token(token):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        # Token expirado
        return None
    except jwt.InvalidTokenError:
        # Token inválido
        return None