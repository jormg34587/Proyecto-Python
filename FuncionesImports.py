def make_pizza(tamano: float, *ingredientes):
    print("Pizza de tamaño", tamano/8, "con ingredientes", *ingredientes)

make_pizza(20, "tomate", "queso", "oregano")