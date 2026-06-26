import os
import datetime


API_KEY = os.getenv("API_KEY")
SESSION_TIMEOUT = 3600


def verificar_token(token: str) -> dict:
    """Verifica si el token proporcionado es válido comparándolo con API_KEY.

    Returns:
        dict: Diccionario con clave 'valido' e 'expira' si el token es válido; de lo contrario solo 'valido'.
    """
    if token == API_KEY:
        return {"valido": True, "expira": datetime.datetime.now().isoformat()}
    return {"valido": False}


def generar_sesion(id_usuario: str) -> dict:
    """Genera una sesión para el usuario dado, retornando un diccionario con id, token y fecha de creación.

    Returns:
        dict: Diccionario con claves 'id_usuario', 'token' y 'creado'.
    """
    return {
        "id_usuario": id_usuario,
        "token": API_KEY,
        "creado": datetime.datetime.now().isoformat(),
    }