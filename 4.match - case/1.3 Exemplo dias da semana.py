
import os
os. system("clear")


#Entrda
dia = int(input("digite o número da semana: "))



#processamento

match dia:
    case 1:
        print ("Domingo \t Final de semana")
    case 2:
        print ("Segunda-Feira: \t Dia útil")
    case 3:
        print ("Terça-Feira: \t Dia útil")
    case 3:
        print ("Quarta-Feira: \t Dia útil")
    case 5:
        print ("Quinta-Feira: \t Dia útil")
    case 6:
        print ("Sexta-feira: \t dia útil")
    case 7:
        print ("Sábado: \t Final de semana")
    case _:
        print ("\mOpção Inválida")

#Saída        
