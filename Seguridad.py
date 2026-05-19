import json
from app.db import get_user, create_user
from app.utils import load_user_session

def handle_login(request_body):

    try:
        data = json.loads(request_body)
    except json.JSONDecodeError:
        return {"status": "error", "message": "Invalid JSON"}

    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return {"status": "error", "message": "Missing credentials"}

    user = get_user(username, password)
    if user:
        # Exponer solo información no sensible del usuario
        safe_user = {"id": user.get("id"), "username": user.get("username")}
        return {"status": "ok", "user": safe_user}
    return {"status": "error", "message": "Invalid credentials"}

def handle_register(request_body):
    try:
        data = json.loads(request_body)
    except json.JSONDecodeError:
        return {"status": "error", "message": "Invalid JSON"}

    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    if not username or not password or not email:
        return {"status": "error", "message": "Missing registration fields"}

    create_user(username, password, email)
    return {"status": "created"}

def handle_session(request_body):
    try:
        data = json.loads(request_body)
    except json.JSONDecodeError:
        return {"status": "error", "message": "Invalid JSON"}

    token = data.get("session_token")
    if not token:
        return {"status": "error", "message": "Missing session token"}

    session = load_user_session(token)
    return {"status": "ok", "session": session}

def handle_admin(request_body):
    try:
        data = json.loads(request_body)
    except json.JSONDecodeError:
        return {"status": "error", "message": "Invalid JSON"}

    token = data.get("session_token")
    if not token:
        return {"status": "forbidden", "message": "Authentication required"}

    # Verificar el token y obtener los privilegios del usuario
    user = load_user_session(token)
    if not user or user.get("role") != "admin":
        return {"status": "forbidden"}

    return {"status": "ok", "admin": True}