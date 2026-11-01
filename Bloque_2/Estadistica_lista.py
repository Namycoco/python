
print("___Estadísticas de números___")
print("*"*50)

numeros=[2,6,78,23,12,67]

#calcular el minimo
minimo=numeros[0]

for n in numeros:
    if n < minimo:
        minimo=n

print("El minimo es: ",minimo)

#calcular el maximo
maximo=numeros[0]

for m in numeros:
    if m > maximo:
        maximo=m

print("El máximo es: ",maximo)

#calcular la media de los numeros
total=0
for me in numeros:
    total +=me 
media= total / len(numeros)
print(f"La media es: {media:.2f}")

#calcular cuantos numeros están por encima de la media
contador=0
for med in numeros:
    if med > media:
        contador +=1

print("Cantidad de números por encima de la media:", contador)