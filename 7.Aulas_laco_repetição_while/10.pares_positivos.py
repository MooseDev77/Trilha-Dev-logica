import os
os.system("cls")
contador = 0
quantidade_impares = 0
quantidade_pares= 0
soma = 0
media_geral = 0


while True:
    numero = int(input("Digite o numero: "))
    if numero == 0:
        break
    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    else:
        quantidade_impares += 1
        
    contador += 1
    soma_geral += numero

media_pares = soma_pares / quantidade_pares
media_geral = soma_geral / contador



print (f"pares: {quantidade_pares}")
print (f"impares: {quantidade_impares}")
print (f"media dos pares: {media_pares}")
print (f"media geral: {media_geral}")
        
        
        
        
             
             