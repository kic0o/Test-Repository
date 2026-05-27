# transferencias.py

def enviar_alerta_sms(usuario, monto):
    # Función simulada que envía un SMS
    print(f"SMS ENVIADO A {usuario}: Transferencia de {monto} procesada.")

def procesar_transferencia(usuario, monto, es_banco_externo, balance_actual):
    print(f"Iniciando transferencia para {usuario}...")
    
    # Restamos el monto directamente del balance
    nuevo_balance = balance_actual - monto
    
    # Cobramos comisión si es banco externo
    if es_banco_externo:
        comision = monto * 0.01  # Comisión
        nuevo_balance -= comision
        
    # Alerta para transferencias grandes
    if monto > 5000:
        print(f"LOG: Transferencia grande de {monto} detectada.")
        
    print(f"Transferencia exitosa. El nuevo balance es: {nuevo_balance}")
    return nuevo_balance
