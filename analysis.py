ventas = [
    {"id": 1, "mes": "Enero", "producto": "Teclado", "categoria": "Periféricos", "cantidad": 2, "precio_unitario": 25.0, "vendedor": "Ana"},
    {"id": 2, "mes": "Enero", "producto": "Ratón", "categoria": "Periféricos", "cantidad": 3, "precio_unitario": 15.0, "vendedor": "Luis"},
    {"id": 3, "mes": "Enero", "producto": "Monitor 24", "categoria": "Pantallas", "cantidad": 1, "precio_unitario": 120.0, "vendedor": "Ana"},
    {"id": 4, "mes": "Enero", "producto": "Auriculares", "categoria": "Audio", "cantidad": 2, "precio_unitario": 40.0, "vendedor": "Marta"},
    {"id": 5, "mes": "Enero", "producto": "SSD 1TB", "categoria": "Almacenamiento", "cantidad": 1, "precio_unitario": 90.0, "vendedor": "Luis"},
    {"id": 6, "mes": "Enero", "producto": "USB 64GB", "categoria": "Almacenamiento", "cantidad": 4, "precio_unitario": 10.0, "vendedor": "Ana"},
    {"id": 7, "mes": "Enero", "producto": "Altavoz", "categoria": "Audio", "cantidad": 1, "precio_unitario": 60.0, "vendedor": "Marta"},
    {"id": 8, "mes": "Febrero", "producto": "Teclado", "categoria": "Periféricos", "cantidad": 1, "precio_unitario": 25.0, "vendedor": "Luis"},
    {"id": 9, "mes": "Febrero", "producto": "Ratón", "categoria": "Periféricos", "cantidad": 5, "precio_unitario": 15.0, "vendedor": "Ana"},
    {"id": 10, "mes": "Febrero", "producto": "Monitor 27", "categoria": "Pantallas", "cantidad": 1, "precio_unitario": 180.0, "vendedor": "Marta"},
    {"id": 11, "mes": "Febrero", "producto": "Auriculares", "categoria": "Audio", "cantidad": 3, "precio_unitario": 40.0, "vendedor": "Luis"},
    {"id": 12, "mes": "Febrero", "producto": "SSD 1TB", "categoria": "Almacenamiento", "cantidad": 2, "precio_unitario": 90.0, "vendedor": "Ana"},
    {"id": 13, "mes": "Febrero", "producto": "USB 64GB", "categoria": "Almacenamiento", "cantidad": 3, "precio_unitario": 10.0, "vendedor": "Marta"},
    {"id": 14, "mes": "Febrero", "producto": "Altavoz", "categoria": "Audio", "cantidad": 2, "precio_unitario": 60.0, "vendedor": "Luis"},
    {"id": 15, "mes": "Marzo", "producto": "Monitor 24", "categoria": "Pantallas", "cantidad": 2, "precio_unitario": 120.0, "vendedor": "Ana"},
    {"id": 16, "mes": "Marzo", "producto": "Teclado", "categoria": "Periféricos", "cantidad": 3, "precio_unitario": 25.0, "vendedor": "Marta"},
    {"id": 17, "mes": "Marzo", "producto": "Auriculares", "categoria": "Audio", "cantidad": 1, "precio_unitario": 40.0, "vendedor": "Luis"},
    {"id": 18, "mes": "Marzo", "producto": "SSD 1TB", "categoria": "Almacenamiento", "cantidad": 1, "precio_unitario": 90.0, "vendedor": "Ana"},
    {"id": 19, "mes": "Marzo", "producto": "USB 64GB", "categoria": "Almacenamiento", "cantidad": 5, "precio_unitario": 10.0, "vendedor": "Marta"},
    {"id": 20, "mes": "Marzo", "producto": "Altavoz", "categoria": "Audio", "cantidad": 1, "precio_unitario": 60.0, "vendedor": "Luis"}
]

#TOTAL FACTURADO
total_facturado = 0
for venta in ventas:
    total_facturado += venta["precio_unitario"] * venta["cantidad"]

print("Total facturado:", total_facturado, "euros")

#TOTAL VENTAS POR CATEGORIA
ventas_por_categoria = {}
for venta in ventas:
    categoria = venta["categoria"]
    if categoria not in ventas_por_categoria:
        ventas_por_categoria[categoria] = 0
    ventas_por_categoria[categoria] += venta["cantidad"] 

facturacion_por_categoria = {}
for venta in ventas:
    categoria = venta["categoria"]
    if categoria not in facturacion_por_categoria:
        facturacion_por_categoria[categoria] = 0
    facturacion_por_categoria[categoria] += venta["cantidad"] * venta["precio_unitario"]

print("Ventas por categoría:")
for categoria, cantidad in ventas_por_categoria.items():
    print(f" - {categoria}: {cantidad} unidades vendidas")

print("Facturación por categoría:")
for categoria, facturacion in facturacion_por_categoria.items():
    print(f" - {categoria}: {facturacion} euros ")

#PRODUCTO MÁS VENDIDO
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    if producto not in ventas_por_producto:
        ventas_por_producto[producto] = 0
    ventas_por_producto[producto] += venta["cantidad"]

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
print(f"Producto más vendido: {producto_mas_vendido} con {ventas_por_producto[producto_mas_vendido]} unidades vendidas")