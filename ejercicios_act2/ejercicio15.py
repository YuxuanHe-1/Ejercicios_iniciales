from math import pi
radio = float(input("Ingrese el radio del cilindro: "))
h = float(input("Ingrese la altura del cilindro: "))
area = 2 * pi * radio ** 2 + 2 * pi * radio * h
volumen = pi * radio ** 2 * h
print(f"Área del cilindro: {round(area, 1)}")
print(f"Volumen del cilindro: {round(volumen, 1)}")