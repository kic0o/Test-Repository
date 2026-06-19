IVA_ESTANDAR = 0.12
IVA_REDUCIDO = 0.07


def calcular_iva_complejo(monto, categoria):
    if categoria == "electronico":
        return monto * IVA_REDUCIDO
    return monto * IVA_ESTANDAR


def calcular_descuento_fidelidad(compras):
    if compras > 10:
        return 0.03
    return 0.0


def obtener_porcentaje_descuento_monto(subtotal):
    if subtotal > 200:
        return 0.10
    elif subtotal > 50:
        return 0.05
    return 0.0
