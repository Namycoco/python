
alumnos={ 

	"Ana":{"Matematicas":4, "Lengua":6, "Historia":9, "Ingles":4}, 
	"Noemi":{"Matematicas":10, "Lengua":9, "Historia":10, "Ingles":8}, 
	"Jose":{"Matematicas":10, "Lengua":8, "Historia":6, "Ingles":10},
	"Eva":{"Matematicas":1, "Lengua":4, "Historia":6, "Ingles":2},
	"Marcos":{"Matematicas":7, "Lengua":5, "Historia":7, "Ingles":8},
}

nombre=input("Introduzca su nombre:")

def evaluacion(alumno, alumnos):
	if alumno in alumnos:
		aprobadas=[]
		suspendidas=[]
   
		for asignatura, nota in alumnos[alumno].items():
			info=f"{asignatura} - Nota: {nota}"
			if nota  >= 5:

				aprobadas.append(info)
			else:
				suspendidas.append(info)
				

		if aprobadas:
 				print(f"{alumno} ha aprobado las siguientes asignaturas:")
		for i, a in enumerate(aprobadas, start=1):
 					print(f"{i}. {a}")

if suspendidas:
    print(f"\n{alumno} ha suspendido las siguientes asignaturas:")
    for i, s in enumerate(suspendidas, start=1):
        print(f"{i}. {s}")

else:
 print(f"No se encontró el alumno {alumno}.")

evaluacion(nombre, alumnos)