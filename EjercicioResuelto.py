"""
Escribe un programa en Python que analice una frase y construya un informe de palabras con las siguientes características:

El usuario introduce una frase.
El programa debe convertir toda la frase a minúsculas, eliminar signos de puntuación comunes (.,;:!?), separar la frase en palabras y contar cuántas veces aparece cada palabra.
Finalmente, debe mostrar las palabras ordenadas de mayor a menor frecuencia.
Si hay palabras con la misma frecuencia, deben mostrarse en orden alfabético.
"""

# Solución:


def informe_palabras(frase):
    # Convertir a minúsculas
    frase = frase.lower()
    # Eliminar signos de puntuación
    for signo in ".,;:!?":
        frase = frase.replace(signo, "")

    palabras = frase.split()

    # Contar ocurrencias
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1

    # Ordenar por frecuencia y luego alfabéticamente
    ordenadas = sorted(conteo.items(), key=lambda x: (-x[1], x[0]))

    print(" Informe de palabras:")
    for palabra, frecuencia in ordenadas:
        print(f"{palabra}: {frecuencia}")


# Ejemplo de ejecución
frase_usuario = input("Ingrese una frase: ")
informe_palabras(frase_usuario)