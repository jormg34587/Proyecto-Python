def isPrimo(num):
    primo = True
    for i in range(2, number):
        if number % i == 0:
            primo = False
            break
    return primo

while True:
    try:
        number = int(input("Introduce un número:"))
        break
    except ValueError:
        print("Introduce un número")

if isPrimo(number):
    print("El número es primo")
else:
    print("No es primo")