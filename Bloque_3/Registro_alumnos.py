import csv

alumnos = [
    ["Nombre", "Edad", "Nota"],
    ["Noemi", 29, 9.5],
    ["Nubia", 20, 9.6],
    ["Ana", 28, 9.7]
    ]

with open("alumnos.csv", "w", newline="") as archivo:
    writer = csv.writer(archivo)
    writer.writerows(alumnos)
    
print("Archivo CSV creado")