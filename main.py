import math

base = int(input('Base del triangulo: \n'))
altura = int(input('Altura del triangulo: \n'))
areaT = (base * altura) // 2
print('El area del triangulo es de', areaT)

radio = int(input('Radio del Circulo: \n'))
areaC = math.pi * (radio**2)
print('El diametro del circulo es de ', areaC)
