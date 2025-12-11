cantidad = int(input("Cuánto quieres invertir: "))
interes = float(input("Introduzca la cantidad de interés anual(en % al año): "))
anos = int(input("Introduzca el número de años: "))
for i in range(1, anos + 1):
    cantidad += cantidad * (interes/100)
    print("Capital año ", i, ": ", cantidad)