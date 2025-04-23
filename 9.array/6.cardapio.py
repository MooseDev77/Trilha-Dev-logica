import os
os.system("clear")

lista_cardapio = []
preco_pratos = []

#Entrda

while True:
    Cardapio = int(input("""" 
  \t Prato \t\t\t Valor
1 \t Picanha \t\t R$ 25,00
2 \t Lasanha \t\t R$ 20,00
3 \t Strogonoff \t\t R$ 18,00
4 \t Bife acebolado \t R$ 15,00
5 \t Pão com ovo \t\t R$5,00
Digite a opção desejada:"""))

    match Cardapio:
        case 1:
            prato = "Picanha"
            comanda = 25.00
        case 2:
            prato = "Lasanha"
            comanda = 20.00
        case 3:
            prato = "Strogonoff"    
            comanda = 18.00
        case 3:
            prato = "bife acebolado"
            comanda = 15.00
        case 5:
            prato = "Pão com ovo"
            comanda = 5.00
        case _:
            print("Opção invalida \nTente novamente!")
            prato = ""
            comanda = 0
    
    lista_cardapio.append(prato)
    preco_pratos.append(comanda)

    continuar = input("Deseja escolher outro prato? \nResponda com 'S' ou 'n' ").lower()
    if continuar == "n":
        break
    os.system("clear")

total_pagar = sum(preco_pratos)

print("\n= Pratos selecionados =")
for prato in lista_cardapio:
    print(f"Prato: {prato} ")

print(f"Total: {total_pagar}")

