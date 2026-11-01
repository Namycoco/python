

agenda={}

def mostrar_menu():
    print("\n--- Agenda ---")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Modificar contacto")
    print("4. Borrar contacto")
    print("5. Mostrar todos los contactos")
    print("6. Salir")
    
def añadir_contacto():
    nombre=input("Introduce el nombre del contacto: ").strip()
    telefono=int(input("Introduce el número de teléfono del contacto: "))
    
    nombre_lower = nombre.lower()
    
    if nombre_lower in agenda:
         print(f"El contacto {nombre} ya existe. Se actualizará el teléfono.")
    agenda[nombre_lower] = telefono
    print(f"Contacto {nombre} añadido/actualizado correctamente.")
        
        
        
def buscar_contacto():
    nombre=input("Introduce el nombre del contacto a buscar: ").strip()
    nombre_lower=nombre.lower()
    
    if nombre_lower in agenda:
        print(f"{nombre}: {agenda[nombre_lower]}.")
    else:
        print(f"No se encuentra el contacto {nombre}.")
        
        
        
def modificar_contacto():
    nombre=input("Introduce el nombre del contacto a modificar: ").strip()
    nombre_lower=nombre.lower()
    
    if nombre_lower in agenda:
        nuevo_telefono=input(f"Introduce el nuevo teléfono para {nombre}: ").strip()
        agenda[nombre_lower]=nuevo_telefono
        print(f"Contacto {nombre} modificado correctamente.")
    else:
        print(f"No se encontró el contacto {nombre}.")
          
    
def borrar_contacto():
    nombre=input("Introduce el nombre del contacto a eliminar: ").strip()
    nombre_lower=nombre.lower()
    
    if nombre_lower in agenda:
        del agenda[nombre_lower]
        print(f"Contacto {nombre} eliminado correctamente.")
    else:
        print(f"No se encontró el contacto {nombre}")
        
def mostrar_contactos():
    
    if agenda:
        print("\n--- Todos los contactos ---")
        for nombre_lower, telefono in agenda.items():
            nombre_mostrar = nombre_lower.title()
            print(f"{nombre_mostrar}: {telefono}")
    else:
        print("No existen contactos en la agenda")
    
    
while True:
    mostrar_menu()
    opcion=input("Elige una opción: ").strip()
    
    if opcion =="1":
        añadir_contacto()
    elif opcion=="2":
        buscar_contacto()
    elif opcion=="3":
        modificar_contacto()
    elif opcion=="4":
        borrar_contacto()
    elif opcion=="5":
        mostrar_contactos()
    elif opcion =="6":
        print("Salir de la agenda")
        break
    else:
         print("Opción no válida. Intenta de nuevo.")
    
