import os
os.system("cls")

soma = 0
contador = 0
Cincok_mulher = 0
acumulo_salario = 0

print ("""
       
    CÓDIGO | DESCRIÇÃO
       1     ADICIONAR PESSOA
       2     EXIBIR RESULTADOS
       3     SAIR   
       
       """)
opcao = int (input("Digite 1 | 2 | 3 para a opção escolhida "))
match opcao:
    
    case '1':
        idade = int(input("Informe sua idade: ")) 
        sexo = str(input("Informe o seu sexo 'M' ou 'F': ")).upper()
        salario = float(input("Informe o seu salario: "))
        acumulo_salario += 1
        contador += 1
        salarial_media = salario / acumulo_salario
    case '2':
        
        print (idade)
        print (sexo)
        print (salario) 
    case '3':
        break
    case _:
        print("Opção Invalida! ")

    
            

                