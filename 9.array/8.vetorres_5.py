import os
os.system("clear")


lista_numeros = []
QUANTIDADE_NUMEROS = 5

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"DIgite o {i+1}° número: "))
    if numero < 0:
       numero = 0
       lista_numeros.append(numero) 
print("\nLISTANDO NÙMEROS")
for numero in lista_numeros:
    print(f"Número: {numero}")