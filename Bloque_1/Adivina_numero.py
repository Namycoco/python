import random

numero_aleatorio = random.randint(1,100)

print("****🎲__Adivina el número aleatorio de máquina__🎲****")
print("*"*50)

intentos=0

while True:
    intento=int(input("Adivina el número entre el 1 y 100 ➔: "))
    intentos +=1
    
    if intento <1 or intento >100:
        print(" ✘ Error, el rango está entre 1 y 100.")
    elif intento < numero_aleatorio:
        print("Demasiado bajo, prueba de nuevo ⌛.")
    elif intento > numero_aleatorio:
        print("Demasiado alto, prueba de nuevo ⌛.")
    else:
        print(f"Enhorabuena, has acertado. el número era {numero_aleatorio} 🍾🏆")
        break

print(f"Has tenido {intentos} intentos para adivinar el número ✔.")
   
    


