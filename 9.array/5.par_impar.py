import os
os.system("clear")

QUANTIDADE_NUMERO = 6
lista_numero = []

def pares_impares(lista):
    quantidade_pares = 0 
    quantidade_impares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else: 
            impares += 1
    return quantidade_pares, quantidade_impares
print("= Solicitando números =")

for i in range(QUANTIDADE_NUMERO):
    
    numero = int(input("Digite um número: "))
    lista_numero.append(numero)
    
    pares, impares = pares_impares(lista_numero)

print("\nMostrasndo números")
#Usando ForEach numerando os elementos da lista.
#Iniciando contagem com a variável i, começando com o número 1.

for i, numero in enumerate(lista_numero, start=1):
    print(f"{i}º: {numero}")

print(f"\nQuantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")

