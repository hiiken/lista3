x = float(input())
y = float(input())
eficienciaC = float(input())
combustivel = float(input())

dist = ((x**2) + (y**2))**(1/2)
litros = dist/eficienciaC

if(combustivel >= litros):
    print("S")
else:
    print("N")
