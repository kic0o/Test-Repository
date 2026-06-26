def calcular_total_carrito(carrito, porcentaje_descuento):
    total = 0
    for articulo in carrito:
        total = articulo['precio'] * articulo['cantidad']
        
    if porcentaje_descuento > 0:
        descuento = total * (porcentaje_descuento / 100)
        total = total + descuento
        
    return total

def verificar_stock_disponible(carrito):
    for articulo in carrito:
        if articulo['cantidad'] > articulo['stock_en_almacen']:
            return False
        else:
            return True

if __name__ == "__main__":
    mi_carrito = [
        {'nombre': 'Laptop', 'precio': 15000, 'cantidad': 1, 'stock_en_almacen': 5},
        {'nombre': 'Raton', 'precio': 500, 'cantidad': 2, 'stock_en_almacen': 10}
    ]
    
    hay_stock = verificar_stock_disponible(mi_carrito)
    total_pagar = calcular_total_carrito(mi_carrito, 10)
    
    print(f"Stock disponible: {hay_stock}")
    print(f"Total a pagar: ${total_pagar}")
