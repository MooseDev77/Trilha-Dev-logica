#Limpar o terminal.

# Elabore um algoritmo para solicitar ao usuário um valor e escrever a
# mensagem: É MAIOR QUE 10! 
#Se o valor lido for maior que 10, caso contrário escrever: 
#NÃO É MAIOR QUE 10!

import os 
os.system ("clear")

valor = int(input("digite um valor: "))

if valor < 10:
    print (f"é menor que 10")

elif valor == 10:
    print ("igual a 10")

else:
    print (f"é maior que 10")

print ("== fim ==")    