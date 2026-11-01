
print("__Bienvenido a la cesta de su compra__")
print("*"*50)

nombre = input("Introduce el nombre del producto: ")



while True:
    precio = float(input("Introduce el precio del producto: "))
    if precio <0:
        print("Error. El precio no puede ser negativo.")
    else:
        break
    
while True:
    cantidad = int(input("Introduce el número de unidades: "))
    if cantidad <0:
        print("Error. La cantidad no puede ser negativa.")
    else:
        break

#calculos:

subtotal=precio*cantidad
iva=subtotal*0.21
total=subtotal+iva


#Salida por pantalla

print("*"*50)
print(f"Total sin IVA: {subtotal:.2f} euros. Unidades a comprar: {cantidad} unidades.")
print(f"Total Final con IVA (21%): {total:.2f} euros.")





