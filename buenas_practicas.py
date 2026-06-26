import datetime


API_KEY = "sk-test-abc123xyzSECRETTOKEN"
SESSION_TIMEOUT = 3600


def verificar_token(token):
    if token == API_KEY:
        return {"valido": True, "expira": datetime.datetime.now().isoformat()}
    return {"valido": False}


def generar_sesion(id_usuario):
    return {
        "id_usuario": id_usuario,
        "token": API_KEY,
        "creado": datetime.datetime.now().isoformat(),
    }
