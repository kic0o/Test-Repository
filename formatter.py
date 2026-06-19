RECARGO_INTERNACIONAL_US = 0.09


def aplicar_tarifa_internacional(total, pais):
    pais_norm = pais.upper()
    if pais_norm == "US":
        return total * (1 + RECARGO_INTERNACIONAL_US)
    return total


def determinar_prioridad(monto):
    if monto > 400:
        return "ALTA"
    elif monto > 100:
        return "NORMAL"
    return "BAJA"


def formatear_precio(monto):
    return f"${monto:,.2f}"


def formatear_resultado(resultado):
    if "error" in resultado:
        return f"[ERROR] {resultado['error']}"
    return (
        f"[OK] Total: {formatear_precio(resultado['total_final'])} "
        f"| Prioridad: {resultado['prioridad']}"
    )
