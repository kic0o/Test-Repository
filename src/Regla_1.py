from utils import sumar, obtener_usuario
from auth import generar_token
import os

def main():
    usuario = obtener_usuario(1)
    total = sumar(5, 10, 15)
    token = generar_token(os.getenv('APP_USER', 'guest'))
    print(f'Token: {token}')
    print(f'Usuario: {usuario}')
    print(f'Total: {total}')

if __name__ == '__main__':
    main()