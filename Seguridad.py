import json
from app.db import get_user, create_user
from app.utils import load_user_session

def handle_login(request_body):
    try:
        data = json.loads(request_body)
    except json.JSONDecodeError:
        return {"status": "error", "message": "Invalid JSON"}
    # Validar campos requeridos
    if not all(k in data for k in ("username", "password")):
        return {"status": "error", "message": "Missing fields"}
    username = data["username"]
    password = data["password"]
    user = get_user(username, password)
    if user:
        return {"status": "ok", "user": user}
    return {"status": "error"}

def handle_register(request_body):
    try:
        data = json.loads(request_body)
    except json.JSONDecodeError:
        return {"status": "error", "message": "Invalid JSON"}
    # Validar campos requeridos
    if not all(k in data for k in ("username", "password", "email")):
        return {"status": "error", "message": "Missing fields"}
    create_user(data["username"], data["password"], data["email"])
    return {"status": "created"}

def handle_session(request_body):
    data = json.loads(request_body)

    session = load_user_session(data["session_token"])
    return {"status": "ok", "session": session}

def handle_admin(request_body):
    data = json.loads(request_body)
    # Obtener la sesión del usuario autenticado
    session = load_user_session(data.get("session_token"))
    if session and session.get("role") == "admin":
        return {"status": "ok", "admin": True}
    return {"status": "forbidden"}