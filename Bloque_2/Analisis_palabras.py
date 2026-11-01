import string

print("__Análisis de Frases__\n")

frase = input("Introduce una frase a analizar:\n").strip()

# Normalizamos la frase
frase_lower = frase.lower()
frase_limpia = frase_lower.translate(str.maketrans('', '', string.punctuation))
palabras = frase_limpia.split()

# Número de palabras
num_palabras = len(palabras)

# Palabras únicas
palabras_unicas = set(palabras)

# Palabra más larga
palabra_mas_larga = max(palabras, key=len)

# Frecuencia de cada palabra
frecuencia = {}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] +=1
    else:
        frecuencia[palabra] = 1
# Imprimimos
print(f"""
Lista de palabras:
{palabras}

Número de palabras:
{num_palabras}

Palabras únicas:
{palabras_unicas}

Palabra más larga:
{palabra_mas_larga}

Frecuencia de cada palabra:
""")
for palabra, cuenta in frecuencia.items():
    print(f"{palabra}: {cuenta}")