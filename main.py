#Hector Andres Alcala Gutierrez

def area_cuadrado(lado: float) -> float:
    return lado * lado

def area_triangulo(base: float, altura: float) -> float:
    return (base * altura) / 2

def area_circulo(radio: float) -> float:
    PI = 3.141592653589793
    return PI * radio * radio

def determinar_zodiaco(dia: int, mes: int) -> str:
    return "zodiaco"

def factorial(numero: int) -> int:
    if(numero == 0):
        return 1
    else:
        return numero * factorial(numero - 1)

def calcular_euler(limite: int) -> float:
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
        print(determinar_zodiaco)

    elif(opcionMenu == 5):
        limiteEuler = int(input("\nDetermine la precision (entero): "))
        print("Euler: " + str(calcular_euler(limiteEuler)))

    elif(opcionMenu == 0):
        print("\nHa salido del programa")

    else:
        print("\nOpcion invalida")