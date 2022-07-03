code = int(input())
password =  int(input())

def validaAcesso(code, password):
    if(code == password):
        print("Saída: Acesso permitido")
    else:
        print("Saída: senha incorreta")

print("Código: {}".format(code))
print("Senha: {}".format(password))
validaAcesso(code, password)
