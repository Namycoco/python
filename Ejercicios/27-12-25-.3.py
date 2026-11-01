#Programa: evaluación de notas.
#Programador: Noemi.
#Fecha modificación:

print("Evaluación de notas")

notas_alumnos=int(input("Introduzca su nota:"))

def evaluacion(notas):
	valoracion="Bien"
	if notas<5:
		valoracion="Suspenso"
	elif notas ==5:
		valoracion="Suficiente"
	elif notas==8:
		valoracion="Notable"
	elif notas>=9:
		valoracion="Sobresaliente"
	return valoracion

print(evaluacion(notas_alumnos))