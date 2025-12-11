# Ejercicio 2
def precioEntrada(edad, estudiante=False, precio_normal=10):
    if edad < 18 or estudiante:
        return precio_normal * 0.5
    return precio_normal


# Ejercicio 3
def multiplicar(*numeros):
    producto = 1
    for n in numeros:
        producto *= n
    return producto


# Ejercicio 4
def multiplicandoUnaSuma(multiplicador, *numeros):
    return sum(numeros) * multiplicador


# Ejercicio 5
def contarArgumentos(*args):
    return len(args)



print(precioEntrada(16))
print(precioEntrada(20, True))
print(precioEntrada(25))

print(multiplicar(2, 3, 4))
print(multiplicandoUnaSuma(3, 1, 2, 3))
print(contarArgumentos(10, 20, 30, 40))
