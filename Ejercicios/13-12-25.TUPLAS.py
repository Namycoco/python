 #//Con "list" convertimos una tupla en una lista.//
#//para convertir una lista en tupla es con "tuple"// milista=["Noemi", "Sara", 13, 2, 1992, 13] mitupla=tuple(milista) print(mitupla)

#// la instrucción "in" busca en la lista y te devuelve un booleano. print("Juan" in mitupla)//
#// el método "count" te cuenta cuantas veces aparece el elemento en la lista. print(mitupla.count(13))
#//Método "len" dice cuantos elementos tiene la tupla. print(len(mitupla))

# DESEMPAQUETADO DE TUPLAS: la tupla guarda elementos y les asigna un lugar: mitupla=("Juan", 13, 2, 1994)nombre, dia, mes, agno= mitupla print(nombre) print(dia) print(mes) print(agno)

mitupla=("Juan", 13, 2, 1994)
milista=list(mitupla)
milista.insert(1,"Sara")
nombre,Nombre, dia, mes, agno= milista
print(nombre)
print(Nombre)
print(dia)
print(mes)
print(agno)