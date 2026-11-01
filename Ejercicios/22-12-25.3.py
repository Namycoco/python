#Programa:introducir datos de dos personas y mostrar la altura mayor o iguales.
#Programador: Noemi.
#Fecha de última modificación:22-12-25.

print("Datos de la primera persona")
nombre1=input("Introduzca su nombre:")
edad1=int(input("Introduzca su edad:"))
altura1=float(input("Introduzca altura:"))


print("Datos de la segunda persona")
nombre2=input("Introduzca su nombre:")
edad2=int(input("Introduzca su edad:"))
altura2=float(input("Introduzca su altura:"))


if altura1==altura2:
    print("Tienen la misma altura:", nombre1, "y", nombre2)

elif altura1>altura2:
    print("Tiene la altura más alta:",nombre1)

else:
    print("Tiene la altura más alta:",nombre2)