import os
os.system("clear")

lista_numero = []
QUANTIDADE_NUMEROS = 5
import time

print("= Solicitando números =")
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista_numero.append(numero)

#Verificando maior e mnor número em uma linha.
#As funçoes max() e min() percorrem o vetor e mostram o maior e
#o mnor npumero respectivamente.
menor = min(lista_numero)
maior = max(lista_numero)

print("\nMostrando números")
#Usandoo forEach numerando os elementos da lista.
#Iniciando contagem com a variárel i, começando com o número 1.
for i, numero in enumerate(lista_numero, start=1):
    print(f"{i}º número: {numero}")
    time.sleep(3)


print(f"Numeros apresentados: {lista_numero}")
print(f"Menor: {menor}")
print(f"Maior: {maior}")
