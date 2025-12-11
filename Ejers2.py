try:
    cantidad = float(input("Introduce una cantidad de dinero(en EUR): "))
    moneda = input("Introduce una moeda para convertir(USD, GBP o JPY):")

    if moneda == "USD".casefold():

        print("La cantidad de dinero es: ", cantidad * 1.17, " dólares")
        
    elif moneda == "GBP".casefold():

        print("La cantidad de dinero es: ", cantidad * 0.87, " libras")

    elif moneda == "JPY".casefold():

        print("La cantidad de dinero es: ", cantidad * 176.07, " yenes")

    else:
        print("Introduce una moneda válida.")

except ValueError as e:

    print("Introduce números, no letras", e)
