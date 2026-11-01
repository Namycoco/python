#Programa: Tablas de multiplicar.
#Programador: Noemi.
#Fecha modificación:

numero=int(input("Introduce un número:")) 

print(f"Tabla de multiplicar {numero}: ") # Esa "f" dentro del texto, reemplaza {nombre} por el valor de la variale nombre, antes se usaba .format(nombre)

for i in range (1,11):
	print(f"{numero} x {i} = {numero*i}")