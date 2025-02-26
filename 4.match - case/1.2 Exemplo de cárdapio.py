import os 
os.system("clear")

#Faça um algoritmo que colicite ao usuário dois número
# e um caractere que calcula as operações basicas 
# e um caractere que calcula as operações basicas 

import os
os. system("clear")


#Entrda
opcao = int(input("""" 
1 \t Prato \t\t\t Valor
2 \t Picanha \t\t R$ 25,00
3 \t lasanha \t\t R$ 20,00
3 \t Strogonoff \t\t R$ 18,00
4 \t bife acebolado \t R$ 15,00
5 \t Pão com ovo \t\t r$5,00

Digite a opção desejada:
"""))

#processamento
match opcao:
    case 1:
        print ("opção desejada:Picanha, 25,00")
    case 2:
        print ("opção desejada:lasanha, 20,00")
    case 3:
        print ("opção desejada:Strognoff, 18,00")
    case 3:
        print ("opção desejada:Bife acebolado, 15,00")
    case 5:
        print ("opção desejada:Pão com ovo, 5,00")
#Saída        
