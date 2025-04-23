import os
os.system("clear")

def inteiro(numero):
    if numero < 0:
        print("Numero negativo.")
    if numero  == 0:
        print("Numero neutro.")
    else: 
        print("Numero positivo.")
numero = int(input("Digite o seu numero: "))
inteiro(numero)
