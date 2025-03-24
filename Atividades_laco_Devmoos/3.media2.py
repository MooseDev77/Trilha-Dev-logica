import os
os.system("cls")

soma = 0 
contador = 0
print("solicitando números")
        
while True:
        QUANTIDADE_PEDIDOS = 5
        contador = 0
        nota = float(input(f"Suas notas cidadão: "))
        resposta = input("Deseja adicionar maus uma nota? \nDigite 's ou 'n'").upper()
  
        
        if resposta == 'n':
                break
        else:
                contador += 1
                soma += nota
        if contador == 0:
                soma = nota 
                contador = 1
media = soma / contador
print(f"\nMédia: {media}")                                
                