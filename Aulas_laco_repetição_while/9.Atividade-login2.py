import os
os.system("cls")

login_cadastrado = 'Moose'
senha_cadastrada = '123'
QUANTIDADE_PEDIDOS = 3
contador = 0  
while True:
    login = input("Digite seu login por favor: ")
    senha = input("Digite sua senha por favor: ")

    if  login == login_cadastrado or senha == senha_cadastrada:
        print("Bem vindo")   
        break

    else: 
          print("Acesso negado. \n")
          contador += 1

    if  contador == 3:      
          print("Você atingiu o limite de tentativas")
          break
    


            

