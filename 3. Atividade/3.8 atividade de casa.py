#Elabore um algoritmo usando operações lógicas para informar se uma pessoa é obrigada a votar.
#Considre que a regra é que menores de 18 e maiores que 65 não são obrigados a votar 

import os
os.system ("clear")

nome = str (input("Informe o seu nome completo: "))
idade = int(input("Informe sua idade: "))


if idade > 65 or idade < 18:
    print("não é obrigado a votar!")
else:
    print("é obrigado a votar!")        

