print("__Calificador de Notas__")


while True:
    nota=float(input("Introduce una nota entre 0 y 10: "))
    if nota < 0 or nota > 10:
        print("Error. La nota debe estar en un rango entre 0 y 10.")
    else:
        break
    
    
if nota <5:
    print(f"Está suspenso. Su nota es de: {nota}")
elif nota <6:
        print(f"Suficiente. Nota: {nota}")
elif nota <7:
        print(f"Bien. Nota: {nota}")
elif nota<9:
        print(f"Notable. Nota: {nota}")
else:
        print(f"Sobresaliente. Nota: {nota}")
