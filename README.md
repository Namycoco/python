# 🐍 PYTHON DESDE CERO

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=14532D&height=120&section=header&text=PYTHON%20DESDE%20CERO&fontSize=40&fontColor=ffffff&animation=fadeIn" width="100%">
</p>

<hr>

<p align="center">
  <img src="https://img.shields.io/badge/Python-Lenguaje_de_programación-2E8B57?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Nivel-Principiante-22C55E?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Aprendizaje-En_progreso-166534?style=for-the-badge" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=22C55E&center=true&vCenter=true&width=650&lines=Aprendiendo+Python+desde+cero;Practicando+programaci%C3%B3n;Desarrollando+mis+habilidades;Cada+l%C3%ADnea+de+c%C3%B3digo+cuenta+%F0%9F%90%8D" />
</p>

---

## 🐍 ¿Qué es Python?

Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. Destaca por tener una sintaxis sencilla y legible, lo que lo convierte en una excelente opción para aprender programación.

Se utiliza en diferentes ámbitos como:

- Desarrollo web.
- Inteligencia artificial y aprendizaje automático.
- Ciencia y análisis de datos.
- Automatización de tareas.
- Desarrollo de aplicaciones.
- Ciberseguridad.

En este repositorio recopilaré mis ejercicios y prácticas de Python, comenzando por los conceptos fundamentales y avanzando progresivamente hacia temas más complejos.

---

## **01. Primeros pasos con Python**

El clásico programa para comenzar a programar:

```python
print("¡Hola, mundo!")
```

**¿Qué significa?**

- `print()`: muestra información por pantalla.
- `"¡Hola, mundo!"`: es el texto que queremos mostrar.
- No es necesario utilizar `;` al final de cada instrucción.

## **02. Variables y tipos de datos**

Las variables permiten almacenar información que podemos utilizar durante la ejecución de un programa.

```python
nombre = "Programador"
edad = 20
altura = 1.75
estudiante = True
inicial = "P"

print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("¿Es estudiante?:", estudiante)
print("Inicial:", inicial)
```

**Principales tipos de datos:**

| Tipo | Descripción | Ejemplo |
|:---|:---|:---|
| `int` | Números enteros | `25` |
| `float` | Números decimales | `3.14` |
| `str` | Cadenas de texto | `"Hola"` |
| `bool` | Verdadero o falso | `True` |
| `complex` | Números complejos | `2 + 3j` |

## **03. Operadores**

Python dispone de diferentes operadores para realizar operaciones matemáticas y comparaciones.

```python
a = 10
b = 3

print(a + b)   # Suma
print(a - b)   # Resta
print(a * b)   # Multiplicación
print(a / b)   # División
print(a // b)  # División entera
print(a % b)   # Módulo
print(a ** b)  # Potencia
```

También existen operadores de comparación (`==`, `!=`, `>`, `<`) y operadores lógicos (`and`, `or`, `not`).

## **04. Condicionales**

Permiten ejecutar diferentes instrucciones dependiendo de si se cumple una condición.

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

También podemos utilizar `elif` para comprobar varias condiciones:

```python
nota = 7

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
```

## **05. Bucles**

Los bucles permiten repetir instrucciones sin tener que escribirlas varias veces.

**Bucle FOR:**

```python
for i in range(1, 6):
    print("Número:", i)
```

**Bucle WHILE:**

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

**Instrucciones importantes:**

- `break`: termina el bucle.
- `continue`: salta a la siguiente iteración.
- `range()`: genera una secuencia de números.

## **06. Entrada de datos por teclado**

Con `input()` podemos solicitar información al usuario.

```python
nombre = input("Introduce tu nombre: ")

print("¡Bienvenido,", nombre, "!")
```

Para trabajar con números podemos utilizar `int()` o `float()`:

```python
edad = int(input("Introduce tu edad: "))

print("El año que viene tendrás:", edad + 1)
```

## **07. Listas, tuplas y diccionarios**

Python dispone de diferentes estructuras para almacenar y organizar información.

**Listas:**

```python
frutas = ["Manzana", "Pera", "Plátano"]

frutas.append("Naranja")

print(frutas)
print(frutas[0])
```

**Tuplas:**

```python
coordenadas = (10, 20)

print(coordenadas)
```

**Diccionarios:**

```python
persona = {
    "nombre": "Alex",
    "edad": 20,
    "ciudad": "Madrid"
}

print(persona["nombre"])
print(persona["edad"])
```

| Estructura | Características |
|:---|:---|
| Lista | Ordenada y modificable. |
| Tupla | Ordenada e inmutable. |
| Conjunto (`set`) | Elementos únicos. |
| Diccionario | Almacena pares clave-valor. |

## **08. Funciones**

Las funciones permiten organizar el código y reutilizar instrucciones.

```python
def saludar(nombre):
    print("¡Hola,", nombre, "!")

saludar("Alex")
```

También podemos devolver resultados utilizando `return`:

```python
def sumar(a, b):
    return a + b

resultado = sumar(10, 5)

print("Resultado:", resultado)
```

## **09. Cadenas de texto (Strings)**

Python ofrece diferentes métodos para trabajar con cadenas de texto.

```python
texto = "aprendiendo python"

print(texto.upper())
print(texto.lower())
print(texto.capitalize())
print(texto.title())
print(len(texto))
print(texto.replace("python", "programación"))
```

## **10. Programación orientada a objetos (POO)**

La programación orientada a objetos permite organizar el código mediante clases y objetos.

**Conceptos principales:**

- Clases: plantillas para crear objetos.
- Objetos: instancias de una clase.
- Atributos: características de los objetos.
- Métodos: funciones definidas dentro de una clase.
- Herencia: permite reutilizar características de otras clases.

**Ejemplo:**

```python
class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre}")

persona = Persona("Alex", 20)

persona.presentarse()
```

## **11. Manejo de excepciones**

Permite controlar errores durante la ejecución de un programa.

```python
try:
    numero = int(input("Introduce un número: "))
    print(10 / numero)

except ValueError:
    print("Debes introducir un número válido")

except ZeroDivisionError:
    print("No puedes dividir entre cero")

finally:
    print("Programa finalizado")
```

## **12. Módulos y librerías**

Los módulos permiten reutilizar código y acceder a funcionalidades adicionales.

```python
import math
import random

print(math.sqrt(25))
print(random.randint(1, 10))
```

---

## 📚 Temario de aprendizaje

Estos son los principales temas que iré trabajando a lo largo del repositorio:

- [ ] Primeros pasos con Python.
- [ ] Variables y tipos de datos.
- [ ] Operadores.
- [ ] Condicionales.
- [ ] Bucles.
- [ ] Entrada y salida de datos.
- [ ] Listas, tuplas, conjuntos y diccionarios.
- [ ] Funciones.
- [ ] Cadenas de texto.
- [ ] Comprensión de listas.
- [ ] Programación orientada a objetos.
- [ ] Manejo de archivos.
- [ ] Excepciones.
- [ ] Módulos y librerías.
- [ ] Programación avanzada.
- [ ] Proyectos prácticos.

## 🎯 Retos para practicar

| Nivel | Ejercicio |
|:---:|:---|
| 🟢 Fácil | Crear una calculadora básica. |
| 🟢 Fácil | Comprobar si un número es par o impar. |
| 🟢 Fácil | Calcular el área de un triángulo. |
| 🟡 Medio | Crear un juego de adivinar números. |
| 🟡 Medio | Crear un conversor de temperaturas. |
| 🟡 Medio | Comprobar si una palabra es palíndroma. |
| 🔴 Difícil | Crear un sistema de gestión de usuarios. |
| 🔴 Difícil | Crear un gestor de tareas. |

---

## 📊 Estadísticas del repositorio

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=TU_USUARIO&show_icons=true&theme=merko&hide_border=true&locale=es" width="48%" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=TU_USUARIO&layout=compact&theme=merko&hide_border=true&locale=es" width="48%" />
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=TU_USUARIO&theme=merko&hide_border=true" width="70%" />
</p>
