lineas = int(input("Ingresa un número de líneas: "))

for i in range(1, lineas + 1):
    espacios = ' ' * (lineas - i)
    asteriscos = '*' * (2 * i - 1)
    print(espacios + asteriscos)

