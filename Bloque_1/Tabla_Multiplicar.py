
print("Tabla de Multiplicar (1-10)")
print("*"*50)
while True:
    entrada=input("Introduce un número entre 1 y 10 (para terminar escribe la palabra: 'Salir'): ")
    if entrada.lower() == "salir":
        break
    numero=int(entrada)
    
    if numero < 1 or numero > 10:
        print("Error. El número debe estar entre 1 y 10.")
        continue
    
    for i in range (1,11):
        print(f"{numero} x {i} = {numero*i}")
        
    