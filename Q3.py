
a = int(input())
b = int(input())
c = int(input())

def verificaTriangulo(a, b, c):
    if(((a**2) + (b**2)) > (c**2)):
        print("A")
    elif(((a**2) + (b**2)) == (c**2)):
        print("R")
    elif(((a**2) + (b**2)) < (c**2)):
        print("O")

verificaTriangulo(a, b, c)
