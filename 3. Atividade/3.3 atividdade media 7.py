#Limpar o terminal.

# Elabore um algoritmo para solicitar ao usuário um valor e escrever a
# mensagem: É MAIOR QUE 10! 
#Se o valor lido for maior que 10, caso contrário escrever: 
#NÃO É MAIOR QUE 10!
#Se o número digitado é igual a 10, caso seja, escreva a mensagem : 
#O número é igual a 10
import os 
os.system ("clear")


nota_1 = float(input("digite um nota 1°: "))
nota_2 = float(input("digite um nota 2°: "))
nota_3 = float(input("digite um nota 3°: "))

soma = nota_1 + nota_2 + nota_3
media = soma / 3 

print(f"media: {media}")

if media < 7: 
    print("reprovado")
else: 
    print("aprovado")



    



   