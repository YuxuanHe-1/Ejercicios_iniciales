a = input()
b = input()
c = input()
d = input()
e = input()
resultado = ""
for i in [a,b,c,d,e][:-1]:
    resultado += i+ "," 
else:
    resultado += e
print(a+b+c+d+e)
print(resultado)