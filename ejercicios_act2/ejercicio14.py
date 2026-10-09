from math import pi
diametro = float(input("Ingrese el diámetro de la esfera: "))
radio = diametro / 2
area = pi * radio ** 2
print(f"Área del círculo: {round(area, 1)}")
print(f"circunferencia: {round(2 * pi * radio, 1)}")