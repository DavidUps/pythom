import os

def clear():
    os.system('cls')

def wait():
    wait = input()

def resul1():
    print("Has dado al 1")
def resul2():
    print("Has dado al 2")
def resul3():
    print("Has dado al 3")
def resul4():
    print("Has dado al 4")

eu50 = 0
eu20 = 0
eu10 = 0
eu5 = 0
eu2 = 0
eu1 = 0
eu05 = 0
eu02 = 0
eu01 = 0
eu005 = 0

resulCase = True

while resulCase:
    print("Elige: \n" + "1.-Consultar Dinero \n" + "2.-Dar Cambio \n" + "3.-Reponer Cambio \n" + "4.-Guardar Estado \n" + "0.-Salir")
    resulCase = input()
    if resulCase == '1':
        resul1()
    if resulCase == '2':
        resul2()
    if resulCase == '3':
        resul3()
    if resulCase == '4':
        resul4()
    if resulCase == '0':
        resulCase = False
    wait()
    clear()
