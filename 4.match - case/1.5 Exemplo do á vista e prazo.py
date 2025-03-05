import os
os. system("clear")

#Entrda
valor = float(input("informe o valor do produto: R$ "))
forma_de_pagamento = int(input("""digite a forma de pagamento: 
1. vista
2. prazo
                               
"""))

parcela = int(input("Digite a quantidade de parcela(até 6x): "))
    

#processamento

match forma_de_pagamento:

    case 1: #Á vista
        desconto = valor * 0.10
        print ("Valor do produto:R$100,00")
        print ("Pagamento a vista")
        print ("Valor do desconto:R$10,00")
        print ("Total a pagar é:R$90,00")
    case 2:
        parcela = valor / 6
        print ("valor do produto:R$100,00")
        print ("pagamento a prazo")
        print ("valor da parcela:R$16,67")
        print ("total a pagar:6x de R$100,00")                       
    case _:
        print ("\mOpção Inválida")                




                
       


    
