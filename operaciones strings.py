# Ejercicio con métodos de cadenas en Python

# 1. Entrada de texto
texto = "   Hola Mundo, bienvenido a Python!   "

# 2. Limpieza de espacios
print("Texto original:", repr(texto))
texto_limpio = texto.strip()
print("Texto limpio:", repr(texto_limpio))

# 3. Transformaciones
print("Mayúsculas:", texto_limpio.upper())
print("Minúsculas:", texto_limpio.lower())
print("Capitalizado:", texto_limpio.capitalize())
print("Título:", texto_limpio.title())
print("Swapcase:", texto_limpio.swapcase())

# 4. Búsqueda y conteo
print("Posición de 'Python':", texto_limpio.find("Python"))
print("Número de veces que aparece 'o':", texto_limpio.count("o"))

# 5. Validaciones
print("¿Es alfabético?:", texto_limpio.isalpha())   # Falso porque tiene espacios y signos
print("¿Empieza con 'Hola'?:", texto_limpio.startswith("Hola"))
print("¿Termina con '!'?:", texto_limpio.endswith("!"))

# 6. División y unión
palabras = texto_limpio.split(" ")
print("Lista de palabras:", palabras)

texto_unido = "-".join(palabras)
print("Texto unido con guiones:", texto_unido)

# 7. Reemplazo
nuevo_texto = texto_limpio.replace("Mundo", "Universo")
print("Texto reemplazado:", nuevo_texto)
