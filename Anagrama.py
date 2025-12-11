frase = "hola pepe"
frase2 = "eepp loha"
contador = 0

frase = frase.lower()
frase2 = frase2.lower()

for i in frase:
    found = False
    for j in frase2:

        if i == j and not found:
            contador += 1
            found = True

if contador == len(frase):
    print("la frase es un anagrama")
else:
    print("la frase no es un anagrama")
