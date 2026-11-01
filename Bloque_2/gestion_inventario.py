inventario= [
    {"Producto": "Lavadora", "Precio": 300, "Stock": 19},
    {"Producto": "Televisión", "Precio": 200, "Stock":3},
    {"Producto": "Nevera", "Precio": 400, "Stock": 2}
    ]

def mostrar_menu():
    print("\n___Gestión de inventario___")
    print("""\nMenú de opciones:
      Opción 1: Añadir productos.
      Opción 2: Buscar por nombre.
      Opción 3: Calcular el valor total de inventario.
      Opción 4: Listar productos con Stock bajo.
      Opción 5: Mostrar todos los Stock.
      Opción 6: Salir del inventario.""")
    
    
def añadir_productos():
    producto=input("Introduce el nombre de un producto: ").strip()
    precio=float(input("Introduce el precio del producto: "))
    stock=int(input("Introduce las unidades existentes del producto: "))    
    
    for item in inventario:
        if item["Producto"].lower() == producto.lower():
          
            item["Precio"] = precio
            item["Stock"] = stock
            print(f"El producto {producto} ya existía. Se ha actualizado el inventario.")
            return
    

    inventario.append({"Producto": producto, "Precio": precio, "Stock": stock})
    print(f"Producto {producto} añadido correctamente.")
    
    
def buscar_nombre():
    producto=input("Introduce el nombre de un producto: ").strip()
    producto_lower = producto.lower()
    
    for item in inventario:
        if item["Producto"].lower() == producto_lower:
            print(f"Producto encontrado: {item['Producto']}, Precio: {item['Precio']} €, Stock: {item['Stock']} unidades")
            return
    
    print(f"El producto {producto} no existe.")

        
def calcular_valor():
    ValorTotal=0
    for producto in inventario:
        ValorTotal += producto["Precio"]* producto["Stock"]
    print(f"\nEl valor total del inventario es: {ValorTotal} €")  

def stock_bajo(inventario, limite=5):
    return [p for p in inventario if p["Stock"] < limite]
            
def mostrar_todo():
    if inventario:
        print("Todos los productos")
        for item in inventario:
            print(f"{item['Producto']}: Precio {item['Precio']} €, Stock {item['Stock']} unidades")
    else:
        print("No existen productos en el inventario")
             

while True:
    mostrar_menu()
    opcion=input("Elige una opción: ").strip()
    
    if opcion=="1":
        añadir_productos()
    elif opcion=="2":
        buscar_nombre()
    elif opcion=="3":
        calcular_valor()
    elif opcion=="4":
        productos_bajo = stock_bajo(inventario)
        if productos_bajo:
            print("\nProductos con stock bajo (menos de 5 unidades):")
            for p in productos_bajo:
                print(f"{p['Producto']}: {p['Stock']} unidades")
        else:
            print("No existen productos con Stock menor de 5 unidades.")
    elif opcion=="5":
        mostrar_todo()
    elif opcion=="6":
        print("Salir del inventario")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
        