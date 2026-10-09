a = input()
b = input()
c = input()
d = input()
e = input()
resultado = ""
for i in [a,b,c,d,e]:
    resultado += i+ ","
print(resultado[:-1])
resultado = ""
for i in [a,b,c,d,e][::-1]:
    resultado += i+ "," 
print(resultado[:-1])
