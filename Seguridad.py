import json
from app.db import get_user, create_user
from app.utils import load_user_session

def handle_login(request_body):

    try:
        data = json.loads(request_body)
    except json.JSONDecodeError:
        return {"status": "invalid_request"}
    username = data.get("username")
    password = data.get("password")
    if not isinstance(username, str) or not isinstance(password, str):
        return {"status": "invalid_request"}
    username = username.strip()

    user = get_user(username, password)
    if user:
        safe_user = {"username": user.get("username"), "email": user.get("email")}
        return {"status": "ok", "user": safe_user}
    return {"status": "error"}

def handle_register(request_body):
    try:
        data = json.loads(request_body)
    except json.JSONDecodeError:
        return {"status": "invalid_request"}
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    if not all(isinstance(x, str) for x in [username, password, email]):
        return {"status": "invalid_request"}
    create_user(username.strip(), password, email.strip())
    return {"status": "created"}

def handle_session(request_body):
    try:
        data = json.loads(request_body)
    except json.JSONDecodeError:
        return {"status": "invalid_request"}
    token = data.get("session_token")
    if not isinstance(token, str):
        return {"status": "invalid_request"}
    token = token.strip()
    session = load_user_session(token)
    return {"status": "ok", "session": session}

def handle_admin(request_body):
    try:
        data = json.loads(request_body)
    except json.JSONDecodeError:
        return {"status": "invalid_request"}
    token = data.get("session_token")
    if not isinstance(token, str):
        return {"status": "invalid_request"}
    token = token.strip()
    session = load_user_session(token)
    if not session or session.get("role") != "admin":
        return {"status": "forbidden"}
    return {"status": "ok", "admin": True}