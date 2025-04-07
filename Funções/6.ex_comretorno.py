import os
os.system("cls")



def somar(numero, numero_2):
    return numero + numero_2

def subtrair(numero, numero_2):
    return numero - numero_2

def multiplicar(numero, numero_2):
    return numero * numero_2

def dividir(numero, numero_2):
    return numero / numero_2

print("= NOTAS =")
numero = int(input("Digite o numero desejado: "))
numero_2 = int(input("Digite o numero desejado: "))

soma = somar(numero, numero_2)
subtracao = subtrair(numero, numero_2)
multiplicao = multiplicar(numero, numero_2)
divisao = dividir(numero, numero_2)

print("\n= Resultados =")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicao}")
print(f"Divisão: {divisao}")