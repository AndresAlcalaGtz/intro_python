#Hector Andres Alcala Gutierrez

def area_cuadrado(lado: float) -> float:
    return lado * lado

def area_triangulo(base: float, altura: float) -> float:
    return (base * altura) / 2

def area_circulo(radio: float) -> float:
    PI = 3.141592653589793
    return PI * radio * radio

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