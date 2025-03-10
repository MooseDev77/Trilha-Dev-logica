import os
os. system("clear")

#Entrda

valor = float(input("informe o valor do produto: R$ "))

forma_de_pagamento = int(input("""digite a forma de pagamento: 
1. vista
2. prazo
                               
""" ))
      
desconto = int(input("confirme pagamento à vista: "))
         
parcela = int(input("Digite a quantidade de parcela(até 6x): "))
    

#processamento

match forma_de_pagamento:

    case 1:
        desconto = valor * 0.10
        print ("Valor do produto:R$100,00")
        print ("Pagamento a vista")
        print ("Valor do desconto:R$10,00")
        print ("Total a pagar é:R$90,00")
    

    case 6:
        parcela = valor / 6
        print ("valor do produto:R$100,00")
        print ("pagamento a prazo")
        print ("valor da parcela:R$16,67")
        print ("total a pagar:R$16,67 de 6x R$100,00 ")                       
    
    
    case 5:
        parcela = valor / 5
        print ("valor do produto:R$100,00")
        print ("pagamento a prazo")
        print ("valor da parcela:R$20,00")
        print ("total a pagar:R$20,00 de 5x R$100,00 ")                 
    
    
    case 4:
        parcela = valor / 4
        print ("valor do produto:R$100,00")
        print ("pagamento a prazo")
        print ("valor da parcela:R$25,00")
        print ("total a pagar:R$25,00 de 4x R$100,00 ")  
    
    
    case 3:
        parcela = valor / 3
        print ("valor do produto:R$100,00")
        print ("pagamento a prazo")
        print ("valor da parcela:R$33,33")
        print ("total a pagar:R$33,33 de 3x R$100,00 ")  
   
   
    case 2:
        parcela = valor / 2
        print ("valor do produto:R$100,00")
        print ("pagamento a prazo")
        print ("valor da parcela:R$50,00")
        print ("total a pagar:R$50,00 de 2x R$100,00 ")              
    
    
    case 1:
        parcela = valor / 1
        print ("valor do produto:R$100,00")
        print ("pagamento a prazo")
        print ("total a pagar:R$100,00 ")  

                
       


    
