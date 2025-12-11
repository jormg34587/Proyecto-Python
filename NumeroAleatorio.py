import random

randNumber = random.randrange(1, 101)

def isCorrectNumber(randNumber, number):
    if randNumber == number:
        return 0
    elif randNumber > number:
        return 1
    elif randNumber < number:
        return 2
    else:
        return -1

while True:
    try:
        attempt = int(input("Introduce un número:"))
        if isCorrectNumber(randNumber, attempt) == 2:
            print("El número a adivinar es más bajo")
        elif isCorrectNumber(randNumber, attempt) == 1:
            print("El número a adivinar es más alto")
        elif isCorrectNumber(randNumber, attempt) == 0:
            print("Has acertado!!!")
            break
    except ValueError:
        print("Introduce solo números")