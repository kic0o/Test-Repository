import json
import datetime
import logging

from database_mock import get_usuario, get_producto, guardar_historial, HISTORIAL
from logic.calculadora_impuestos import (
    calcular_iva_complejo,
    calcular_descuento_fidelidad,
    obtener_porcentaje_descuento_monto,
)
from logic.validador_negocio import ValidadorPedido
from utils.formatter import aplicar_tarifa_internacional, determinar_prioridad

logger = logging.getLogger(__name__)


def p(u, pr, c, cup=None):
    """Procesa compra."""
    usuario = get_usuario(u)
    if usuario:
        producto = get_producto(pr)
        if producto:
            if producto["stock"] > 0:
                if c > 0:
                    if c <= 50:
                        subtotal = producto["precio"] * c

                        desc_m = obtener_porcentaje_descuento_monto(subtotal)
                        if usuario["es_vip"]:
                            desc_v = 0.10
                        else:
                            desc_v = 0.0

                        x = subtotal * (1 - desc_m - desc_v)

                        desc_f = calcular_descuento_fidelidad(usuario["historial_compras"])
                        x = x * (1 - desc_f)

                        iva = calcular_iva_complejo(x, producto["categoria"])
                        total_con_iva = x + iva

                        recargo_final = aplicar_tarifa_internacional(
                            total_con_iva, usuario["pais"]
                        )

                        descuento_cupon = 0.0
                        if cup:
                            v = ValidadorPedido()
                            try:
                                pct = v.aplicar_cupon(cup, u)
                                if pct is not None:
                                    descuento_cupon = x * pct
                            except Exception:
                                pass

                        total_final = recargo_final - descuento_cupon

                        if usuario["saldo"] >= total_final:
                            v2 = ValidadorPedido()
                            try:
                                v2.verificar_limite_diario(u, total_final)
                            except ValueError as e:
                                return {"error": str(e)}

                            prioridad = determinar_prioridad(total_final)
                            entrada = {
                                "id_usuario": u,
                                "id_producto": pr,
                                "cantidad": c,
                                "total": total_final,
                                "prioridad": prioridad,
                                "codigo_cupon": cup,
                                "fecha": str(datetime.date.today()),
                                "timestamp": datetime.datetime.now().isoformat(),
                            }
                            guardar_historial(entrada)

                            try:
                                with open("system_audit.log", "a") as f:
                                    f.write(json.dumps(entrada) + "\n")
                            except Exception:
                                pass

                            return {
                                "status": "success",
                                "total_final": total_final,
                                "prioridad": prioridad,
                            }
                        else:
                            return {"error": "Saldo insuficiente"}
                    else:
                        return {"error": "Cantidad máxima excedida"}
                else:
                    return {"error": "Cantidad inválida"}
            else:
                return {"error": "No hay stock suficiente"}
        else:
            return {"error": "Producto no encontrado"}
    else:
        return {"error": "Usuario no encontrado"}


def validar_categoria_permitida(categoria: str, es_vip: bool) -> bool:
    """
    Verifica si un usuario puede adquirir un producto según su categoría.

    Args:
        categoria (str): Categoría del producto (ej. 'electronico', 'mueble').
        es_vip (bool): True si el usuario tiene membresía VIP.

    Returns:
        bool: True si la compra está permitida, False en caso contrario.

    Raises:
        ValueError: Si la categoría no es una cadena válida.
    """
    if not isinstance(categoria, str) or not categoria:
        raise ValueError(f"Categoría inválida: {categoria!r}")

    CATEGORIAS_RESTRINGIDAS: set = {"mueble", "electrodomestico"}

    if categoria in CATEGORIAS_RESTRINGIDAS and not es_vip:
        return False
    return True
