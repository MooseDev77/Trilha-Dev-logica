import os 
os.system ("cls")

Comanda = 0            
while True:
        opcao = int(input("""" 
    1 \t Prato \t\t\t Valor
    2 \t Picanha \t\t R$ 25,00
    3 \t lasanha \t\t R$ 20,00
    4 \t Strogonoff \t\t R$ 18,00
    5 \t bife acebolado \t R$ 15,00
    6 \t Pão com ovo \t\t R$5,00

    Digite a opção desejada:
"""))
        
        match opcao: 
                case 1:
                        prato = "Picanha"
                        preco = 25
                case 2:
                        prato = "lasanha"
                        preco = 20
                case 3: 
                        prato = "strognoff"
                        preco = 18
                case 4: 
                        prato = "bife acebolado"
                        preco = 15
                case 5:
                        prato = "pão com ovo"
                        preco = 5
                        
                        soma += preco                                                                                
                        continuar = input("Quer escolher outra opção? \nDigite 's' ou 'n': ").lower()
                        if continuar == "n":
                                break
                        os.system("cls")