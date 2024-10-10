# HACER CARRITO DE COMPRAS CON ITEM - PRECIO - CANTIDAD

item = input("Que quieres comprar?: ")
precio = float(input("Cual es el precio?: "))
cantidad = int(input("Cuantos queres llevar?: "))
total = precio * cantidad
print(f"El precio es: ${total}")