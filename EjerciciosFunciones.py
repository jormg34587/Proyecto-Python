# Ejercicio 1
def saludar(nombre: str, saludo: str = "Hola"):
    return f"{saludo} {nombre}"

# Ejercicio 2
def calcular_precio(precio_base: float, iva: float = 21):
    return precio_base * (1 + iva / 100)

# Ejercicio 3
def crear_usuario(nombre: str, email: str, activo: bool = True):
    if activo:
        return [nombre, email, activo]
    return []

# Ejercicio 4
def formatear_nombre(nombre: str, apellido: str, orden: str = "nombre_apellido"):
    if orden == "apellido_nombre":
        return f"{apellido} {nombre}"
    return f"{nombre} {apellido}"

# Ejercicio 5
def calcular_descuento(precio_original: float, descuento: float = 10):
    return precio_original * (1 - descuento / 100)

# Ejercicio 7
def filtrar_pares(lista_numeros: list):
    return [num for num in lista_numeros if num % 2 == 0]

# Ejercicio 8
def tabla_multiplicar(numero: int, hasta: int = 10):
    return [numero * i for i in range(1, hasta + 1)]


print(saludar("Juan"))
print(calcular_precio(100))
print(crear_usuario("Ana", "ana@example.com"))
print(formatear_nombre("Carlos", "Pérez", "apellido_nombre"))
print(calcular_descuento(200))
print(filtrar_pares([1, 2, 3, 4, 5]))
print(tabla_multiplicar(5, 5))
