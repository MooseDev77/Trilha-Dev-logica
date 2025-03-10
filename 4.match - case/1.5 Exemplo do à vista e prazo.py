import os
os. system("clear")

#Entrda

valor = float(input("informe o valor do produto: "))
forma_de_pagamento = int(input("""digite a forma de pagamento: 
1. vista
2. prazo
                               
""" ))
      

#processamento

match forma_de_pagamento:

    case 1:
        desconto = valor * 0.10
        valor_pagar = valor_produto - desconto

        #exibindo resultado.
        print(f"\nvalor do produto: R$ {valor_produto}")
        print(f"forma de pagamento: à vista")
        print(f"valor do desconto: R$ {desconto}")
        print(f"total a pagar: R$ {valor_pagar}")
    case 2:
        quantidade_parcelas = int(input("Digite a quantidade de parcelas: "))
        if quantidade_parcelas >= 1 and quantidade_parcelas <= 6:
            valor_parcela = valor_produto / quantidade_parcelas

         #exibindo resultado.
        print(f"\nvalor do produto R$ {valor_produto}")
        print(f"forma de pagamento: à prazo")
        print(f"Quantidade de parcelas {quantidade_parcelas}")                       
        print(f"valor por parcela: R$ {valor_parcela: .2f}")
        print(f"Total à prazo: R$ {valor_produto}")     
   
       else:
        print("O parcelamento deve ser em até 6 parcelas")

    case _:
        print("Opção inválida")

    
