def tablaMultiplicar(num):
    for i in range(1, 11):
        print(i, " * ", num, " = ", i * num)

while True:
    try:
        number = int(input("Ingresa un número(-1 para salir): "))
        if number == -1:
            break
        tablaMultiplicar(number)

    except ValueError:
        print("Introduce números")