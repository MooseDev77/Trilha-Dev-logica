import os 
os.system("cls")

def aparies(numero):
    if numero % 2 == 1:
        print(f"{numero} é ímpar")
    else:
        print(f"{numero} é par")      
numero = int(input("Digite o numero: "))
aparies(numero)  