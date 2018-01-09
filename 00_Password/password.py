password = ''

print("Escriba la contraseña: ")
password = input()
if len(password) < 8 :
    print("Contraseña invalida")
else:
    print("Contraseña valida")

for i in len(password):
    print("Yeii")
