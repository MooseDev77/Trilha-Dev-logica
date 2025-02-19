#Limpar o terminal.
import os 
os.system ("clear")
#Elabore um algoritmo para solicitar dois números e ao final mostre
#na tela 
#A média, a soma, o produto, o menor valor e o maior valor.
#Usando uma linha para cada resultado.

Primeiro_numero =float(input("Digite seu 1°numero:"))
Segundo_numero = float(input("digite seu 2°numero:"))

media = (Primeiro_numero + Segundo_numero) / 2

produto = Segundo_numero * Segundo_numero

menor = min(Primeiro_numero, Segundo_numero)
maior = max(Primeiro_numero, Segundo_numero)

print("\nExibindo resultados:")
print(f"media: {media}")
print(f"produto: {produto}")
print(f"menor: {menor}")
print(f"maior: {maior}")



                               


    



   