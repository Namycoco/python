#Programa: Calculadora.
#Programador: Noemí.
#Fecha modificación:

def calculadora():

	print("Bienvenido a la calculadora Básica")
	print("Operaciones disponibles:")
	print("1.sumar")
	print("2.restar")
	print("3.multiplicar")
	print("4.dividir")

	opcion=input("Elige una operación (1/2/3/4):")

	num1=float(input("Introduce el primer número:"))
	num2=float(input("Introduce el segundo número:"))

	if opcion =="1":
		print("Resultado:", num1 + num2)

	elif opcion == "2":
		print("Resultado:", num1 - num2)

	elif opcion == "3":
		print("Resultado:", num1*num2)

	elif opcion == "4":
		if num2 != 0:
			print("Resultado:", num1/num2)
		else:
			print("Error: no se puede dividir entre 0")
	

calculadora()