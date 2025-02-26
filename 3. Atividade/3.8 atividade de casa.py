#Elabore um algoritmo usando operações lógicas para informar se uma pessoa é obrigada a votar.
#Considre que a regra é que menores de 18 e maiores que 65 não são obrigados a votar 

import os
os.system ("clear")

nome = input("Informe o seu nome completo: ")
idade = int(input("Informe sua idade: "))


if idade > 65:
    print(f"Não é obrigado a votar!")
if idade < 18:
    print(f"Não é obrigado a votar!")
else:
    print(f"É obrigado a votar!")
    