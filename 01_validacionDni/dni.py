
letras = "trwagmy"

numero = int(input("Escribe tu dni: "))
numero = numero % 23
letra = input("Escribe tu letra: ")
if letra == letras[numero]:
    print("Tu DNI es correcto")
else:
    print("La letra de que corresponde a ese DNI es: " + letras[numero] +"\n" + "la que tú as puesto es: " + letra)
