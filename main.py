#Hector Andres Alcala Gutierrez

def area_cuadrado(lado: float):
    if(lado > 0): 
        return lado * lado
    else:
        return "ERROR"

def area_triangulo(base: float, altura: float):
    if((base > 0) and (altura > 0)):
        return (base * altura) / 2
    else:
        return "ERROR"

def area_circulo(radio: float):
    if(radio > 0): 
        PI = 3.1415926535897931
        return PI * radio * radio
    else:
        return "ERROR"

def determinar_zodiaco(dia: int, mes: int)  -> str:
    if(mes == 1):
        if((dia >= 1) and (dia <= 20)): return "Capricornio"
        elif((dia >= 21) and (dia <= 31)): return "Acuario"
        else: return "ERROR"
    elif (mes == 2):
        if((dia >= 1) and (dia <= 19)): return "Acuario"
        elif((dia >= 20) and (dia <= 29)): return "Piscis"
        else: return "ERROR"
    elif(mes == 3):
        if((dia >= 1) and (dia <= 20)): return "Piscis"
        elif((dia >= 21) and (dia <= 31)): return "Aries"
        else: return "ERROR"
    elif(mes == 4):
        if((dia >= 1) and (dia <= 20)): return "Aries"
        elif((dia >= 21) and (dia <= 31)): return "Tauro"
        else: return "ERROR"
    elif(mes == 5):
        if((dia >= 1) and (dia <= 21)): return "Tauro"
        elif((dia >= 22) and (dia <= 31)): return "Geminis"
        else: return "ERROR"
    elif(mes == 6):
        if((dia >= 1) and (dia <= 21)): return "Geminis"
        elif((dia >= 22) and (dia <= 31)): return "Cancer"
        else: return "ERROR"
    elif(mes == 7):
        if((dia >= 1) and (dia <= 22)): return "Cancer"
        elif((dia >= 23) and (dia <= 31)): return "Leo"
        else: return "ERROR"
    elif(mes == 8):
        if((dia >= 1) and (dia <= 23)): return "Leo"
        elif((dia >= 24) and (dia <= 31)): return "Virgo"
        else: return "ERROR"
    elif(mes == 9):
        if((dia >= 1) and (dia <= 23)): return "Virgo"
        elif((dia >= 24) and (dia <= 31)): return "Libra"
        else: return "ERROR"
    elif(mes == 10):
        if((dia >= 1) and (dia <= 23)): return "Libra"
        elif((dia >= 24) and (dia <= 31)): return "Escorpio"
        else: return "ERROR"
    elif(mes == 11):
        if((dia >= 1) and (dia <= 22)): return "Escorpio"
        elif((dia >= 23) and (dia <= 31)): return "Sagitario"
        else: return "ERROR"
    elif(mes == 12):
        if((dia >= 1) and (dia <= 21)): return "Sagitario"
        elif((dia >= 22) and (dia <= 31)): return "Capricornio"
        else: return "ERROR"
    else:
        return "ERROR"


def factorial(numero: int) -> int:
    if(numero == 0):
        return 1
    else:
        return numero * factorial(numero - 1)

def calcular_euler(limite: int):
    if(limite < 0):
        return "ERROR"
    else:
        e = 0
        n = 0
        while n < limite:
            e += 1 / factorial(n)
            n += 1
        return e


opcionMenu = -1
while opcionMenu != 0:
    print("\n\nINTRODUCCION A PYTHON")
    print("1) Calcular el area de un cuadrado")
    print("2) Calcular el area de un triangulo")
    print("3) Calcular el area de un circulo")
    print("4) Determinar un signo zodiacal")
    print("5) Calcular euler")
    print("0) Salir")
    opcionMenu = int(input("Opcion: "))

    if(opcionMenu == 1):
        ladoCuadrado = float(input("\nLado: "))
        print("Area: " + str(area_cuadrado(ladoCuadrado)))

    elif(opcionMenu == 2):
        baseTriangulo = float(input("\nBase: "))
        alturaTriangulo = float(input("Altura: "))
        print("Area: " + str(area_triangulo(baseTriangulo, alturaTriangulo)))

    elif(opcionMenu == 3):
        radioCirculo = float(input("\nRadio: "))
        print("Area: " + str(area_circulo(radioCirculo)))
    
    elif(opcionMenu == 4):
        diaZodiaco = int(input("\nDia (numero): "))
        mesZodiaco = int(input("Mes (numero): "))
        print("Zodiaco: " + str(determinar_zodiaco(diaZodiaco, mesZodiaco)))

    elif(opcionMenu == 5):
        limiteEuler = int(input("\nDetermine la precision (entero): "))
        print("Euler: " + str(calcular_euler(limiteEuler)))

    elif(opcionMenu == 0):
        print("\nHa salido del programa")

    else:
        print("\nOpcion invalida")