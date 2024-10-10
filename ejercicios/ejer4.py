# CALCULAR EL AREA DE UN CIRCULO
import math

radio = float(input("Ingresa el radio: "))

area = math.pi * pow(radio, 2)

print(f"El area es: {round(area, 2)}")