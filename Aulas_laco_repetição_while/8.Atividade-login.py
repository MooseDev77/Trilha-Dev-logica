import os
os.system("cls")

login_cadastrado = 'Moose'
senha_cadastrada = '123'

while True:
    login = input("Digite seu login por favor: ")
    senha = input("Digite sua senha por favor: ")
    if  login != login_cadastrado or senha != senha_cadastrada:
        print("/nLogin invalido. \n")
       
    else: 
        print("Bem vindo")   
        break
    
            

