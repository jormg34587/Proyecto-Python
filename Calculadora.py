def operation(num1, num2, type):
    if type == "+":
        print(num1 + num2)
    elif type == "-":
        print(num1 - num2)
    elif type == "/":
        print(num1 / num2)
    elif type == "*":
        print(num1 * num2)
    else:
        print("Introduce un operador válido")


while True:
    try:
        operacion = input("Ingresa una operacion(*, +, -, /) o introduce \"salir\" para salir del programa: ")
        if operacion == "salir":
            break

        num1 = int(input("Ingresa un numero: "))
        num2 = int(input("Ingresa otro numero: "))


        operation(num1, num2, operacion)

    except ValueError:
        print("Please enter a valid input")
    except ZeroDivisionError:
        print("Division by zero can't be performed.")

