import logging

# Configuración básica para que los logs se vean limpios en consola
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def enviar_alerta_sms(usuario: str, monto: float) -> None:
    """Función simulada que envía un SMS al cliente."""
    logging.info(f"SMS ENVIADO A {usuario}: Transferencia de {monto} procesada.")

def procesar_transferencia(usuario: str, monto: float, es_banco_externo: bool, balance_actual: float) -> float:
    
    logging.info(f"Iniciando transferencia para {usuario}...")
    
    comision = monto * 0.01 if es_banco_externo else 0.0
    
    nuevo_balance = balance_actual - (monto + comision)
    
    if monto > 5000:
        logging.info(f"LOG: Transferencia grande de {monto} detectada. (Se olvidaron de mandar el SMS)")
        
    logging.info(f"Transferencia exitosa. El nuevo balance es: {nuevo_balance}")
    return nuevo_balance

# =================================================================
# ZONA DE SIMULACIÓN Y PRUEBAS AUTOMÁTICAS
# Este bloque permite que el código compile y se pruebe por sí solo
# =================================================================
if __name__ == "__main__":
    print("\n🏦 --- INICIANDO PRUEBAS DE SISTEMA BANCARIO --- 🏦")
    
    casos_prueba = [
        {"desc": "1. Transferencia normal ($2,000)", "usuario": "Alice", "monto": 2000, "ext": False, "balance": 5000},
        {"desc": "2. Banco externo (Debería cobrar 2%)", "usuario": "Bob", "monto": 1000, "ext": True, "balance": 1500},
        {"desc": "3. Alerta Antifraude (Monto de $6,000)", "usuario": "Charlie", "monto": 6000, "ext": False, "balance": 10000},
        {"desc": "4. Límite Excedido (Intenta $15,000)", "usuario": "Diana", "monto": 15000, "ext": False, "balance": 20000},
        {"desc": "5. Saldo Insuficiente (Tiene $1,000, manda $4,000)", "usuario": "Eve", "monto": 4000, "ext": False, "balance": 1000},
    ]
    
    for caso in casos_prueba:
        print(f"\n>> PRUEBA: {caso['desc']}")
        try:
            saldo_final = procesar_transferencia(
                usuario=caso["usuario"], 
                monto=caso["monto"], 
                es_banco_externo=caso["ext"], 
                balance_actual=caso["balance"]
            )
            print(f"✅ ESTADO FINAL: Saldo restante: {saldo_final}")
        except Exception as e:
            
            print(f"❌ TRANSACCIÓN RECHAZADA INTENCIONALMENTE: {type(e).__name__} -> {e}")
            
    print("\n---------------------------------------------------")
