import os
os.system("cls")

def inteiro(numero):
    if numero < 0:
        print("Numero negativo.")
    if numero  >= 0:
        print("Numero neutro.")
    else: 
        print("Numero positivo.")
numero = int(input("Digite o seu numero: "))
inteiro(numero)
