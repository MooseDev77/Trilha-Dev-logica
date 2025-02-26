import os
os. system("clear")

#Entrda
valor = float("digite o valor do produto")
forma_de_pagamento = int (input("""digite a forma de pagamento
1. vista
2. prazo
Digite a forma de pagamento: """))
parcela = int("Digite a quantidade de parcela")

#processamento

match forma_de_pagamento:

    case 1:
        desconto = valor * 0.10
        print ("Pagamento a vista")
    case 2:
        print ("pagamento a prazo")
        
       

match parcela:

    case 1: 
        print("1° parcela")
    case 2:   
        print("2° parcela")
    case 3:    
        print("3° parcela")
    case 4:    
        print("4° parcela")
    case 5:    
        print("5° parcela")
    case 6:    
        print("6° parcela")


    
