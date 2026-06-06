import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def enviar_alerta_sms(usuario: str, monto: float) -> None:
    """Envía un SMS de alerta al usuario cuando se procesa una transferencia.

    Args:
        usuario (str): Identificador del usuario destinatario.
        monto (float): Monto de la transferencia.
    """
    logger.info(f"SMS ENVIADO A {usuario}: Transferencia de {monto} procesada.")

def procesar_transferencia(usuario: str, monto: float, es_banco_externo: bool, balance_actual: float) -> float:
    """Procesa una transferencia bancaria, cobrando comisión si es externo y actualizando el balance.

    Args:
        usuario (str): Identificador del usuario.
        monto (float): Monto a transferir.
        es_banco_externo (bool): Indica si el destino es un banco externo.
        balance_actual (float): Balance actual del usuario.

    Returns:
        float: Nuevo balance tras la transferencia.

    Raises:
        ValueError: Si los parámetros son inválidos o fondos insuficientes.
    """
    if monto <= 0:
        logger.error("Monto de transferencia inválido: debe ser mayor que 0.")
        raise ValueError("El monto de transferencia debe ser mayor que 0.")
    if balance_actual < monto:
        logger.error(f"Fondos insuficientes: balance_actual={balance_actual}, monto={monto}")
        raise ValueError("Fondos insuficientes para realizar la transferencia.")

    logger.info(f"Iniciando transferencia para {usuario} por monto {monto}...")

    comision = 0.0
    if es_banco_externo:
        comision = monto * 0.01
        logger.debug(f"Comisión aplicada por banco externo: {comision}")

    if balance_actual < monto + comision:
        logger.error(f"Fondos insuficientes al considerar comisión: balance_actual={balance_actual}, monto+comision={monto+comision}")
        raise ValueError("Fondos insuficientes tras aplicar la comisión.")

    nuevo_balance = balance_actual - monto - comision

    if monto > 5000:
        logger.warning(f"Transferencia grande detectada: monto={monto}")

    logger.info(f"Transferencia exitosa. Nuevo balance: {nuevo_balance}")
    enviar_alerta_sms(usuario, monto)
    return nuevo_balance