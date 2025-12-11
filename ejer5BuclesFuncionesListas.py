# Definimos las opciones de menú y sus precios
platos = ['Plato 1', 'Plato 2', 'Plato 3']
bebidas = ['Bebida 1', 'Bebida 2', 'Bebida 3']
complementos = ['Complemento 1', 'Complemento 2', 'Complemento 3']
precios_plato = [10, 12, 14]  # Precios de los platos
precios_bebida = [2, 3, 2.5]  # Precios de las bebidas
precios_complemento = [3, 2, 4]  # Precios de los complementos


# Función para mostrar opciones y pedir elección
def elegir_opcion(lista_opciones, mensaje):
    print(mensaje)
    for i, opcion in enumerate(lista_opciones, 1):
        print(f"{i}. {opcion}")
    eleccion = int(input("Introduce el número de tu elección: "))
    return eleccion - 1  # Devolvemos el índice (0 basado)


# Función para calcular el total del pedido
def calcular_total(plato, bebida, complemento, metodo_pago):
    total = precios_plato[plato] + precios_bebida[bebida] + precios_complemento[complemento]
    print("\nResumen de tu pedido:")
    print(f"Plato: {platos[plato]} - {precios_plato[plato]}€")
    print(f"Bebida: {bebidas[bebida]} - {precios_bebida[bebida]}€")
    print(f"Complemento: {complementos[complemento]} - {precios_complemento[complemento]}€")
    print(f"Total: {total}€")

    if metodo_pago == 'efectivo':
        print("Has elegido pagar en efectivo.")
    else:
        print("Has elegido pagar con tarjeta.")
    return total


# Función principal que gestiona el flujo del pedido
def montar_menu():
    print("Bienvenido al montador de menú rápido.")

    # Elegir plato
    plato = elegir_opcion(platos, "Elige un plato:")

    # Elegir bebida
    bebida = elegir_opcion(bebidas, "Elige una bebida:")

    # Elegir complemento
    complemento = elegir_opcion(complementos, "Elige un complemento:")

    # Elegir método de pago
    metodo_pago = input("¿Cómo deseas pagar? (efectivo/tarjeta): ").strip().lower()

    # Validar método de pago
    while metodo_pago not in ['efectivo', 'tarjeta']:
        metodo_pago = input("Por favor, elige un método de pago válido (efectivo/tarjeta): ").strip().lower()

    # Calcular el total
    total = calcular_total(plato, bebida, complemento, metodo_pago)

    # Finalizar
    print("\nGracias por tu pedido. ¡Que disfrutes tu comida!")


# Llamada a la función principal para ejecutar el programa
montar_menu()
