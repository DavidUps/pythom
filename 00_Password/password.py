
longi = False
mayus = False
minus = False
num = False

print("Escriba la contraseña: ")

password = input()

if len(password) > 8:
    longi = True

for letra in password:
    if letra.isupper():
        mayus = True

for letra in password:
    if letra.islower():
        minus = True

for letra in password:
    if letra.isdigit():
        num = True

if longi and mayus and minus and num:
    print("Contraseña corecta")
else:
    print("Revisa la contraseña")
