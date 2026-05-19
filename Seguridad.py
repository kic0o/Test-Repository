import json
from app.db import get_user, create_user
from app.utils import load_user_session

def handle_login(request_body):

    data = json.loads(request_body)
    username = data["username"]
    password = data["password"]

    user = get_user(username, password)
    if user:

        return {"status": "ok", "user": user}
    return {"status": "error"}

def handle_register(request_body):
    data = json.loads(request_body)

    create_user(data["username"], data["password"], data["email"])
    return {"status": "created"}

def handle_session(request_body):
    data = json.loads(request_body)

    session = load_user_session(data["session_token"])
    return {"status": "ok", "session": session}

def handle_admin(request_body):
    data = json.loads(request_body)
    session_token = data.get("session_token")
    if not session_token:
        return {"status": "forbidden"}
    # Verificar la sesión y obtener el rol del usuario de forma segura
    user = load_user_session(session_token)
    if user and user.get("role") == "admin":
        return {"status": "ok", "admin": True}
    return {"status": "forbidden"}