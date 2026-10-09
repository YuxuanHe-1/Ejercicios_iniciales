m = float(input(""))
h = float(input(""))
imc = m / (h ** 2)
print(f"si pesas {m}kg y mides {h}m, ti imc es {round(imc,2)}.{" Hay sobrepeso" if imc > 25 else ""}")