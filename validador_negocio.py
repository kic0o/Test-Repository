import datetime
from database_mock import HISTORIAL, get_cupon


class ValidadorPedido:

    def validar_categoria_permitida(self, categoria, flag):
        categorias_restringidas = ["mueble", "electrodomestico"]
        if categoria in categorias_restringidas:
            if not flag:
                return False
        return True

    def aplicar_cupon(self, codigo, id_usuario):
        try:
            cupon = get_cupon(codigo)
            if cupon is None:
                raise KeyError(f"Cupón {codigo} no existe")
            if not cupon["activo"]:
                raise ValueError("El cupón ingresado está desactivado")
            for compra in HISTORIAL:
                if compra.get("id_usuario") == id_usuario and compra.get("codigo_cupon") == codigo:
                    raise ValueError("El cupón ya ha sido utilizado por este usuario")
            return cupon["porcentaje"]
        except Exception:
            pass

    def verificar_limite_diario(self, id_usuario, monto_nuevo):
        try:
            hoy = datetime.date.today()
            gasto_hoy = sum(
                c["total"] for c in HISTORIAL
                if c["id_usuario"] == id_usuario and c["fecha"] == str(hoy)
            )
            if gasto_hoy + monto_nuevo > 3000:
                raise ValueError("Límite de gasto diario alcanzado")
            return True
        except Exception as e:
            raise e
