import os
import time

os.system("clear")
contador = 0 
soma_salario = 0
maior_idade = 0 
menor_idade = 9999
mulheres5kk = 0

while True:
    print ("""
       
    CÓDIGO | DESCRIÇÃO
       1     ADICIONAR PESSOA
       2     EXIBIR RESULTADOS
       3     SAIR   
       
""")
    opcao = int (input("Digite 1 | 2 | 3 para a opção escolhida: "))

    match opcao:
        case 1:
            idade = int(input("Informe a sua idade: "))
            sexo = input("Informe seu sexo (M/F): ").strip().upper()
            salario = float(input("Informe seu salario, por favor: "))
            contador += 1
            soma_salario += salario
            maior_idade = max(maior_idade, idade)
            menor_idade = min(menor_idade, idade)
            if sexo == "F" and salario >- 5000:
                mulheres5kk += 1
            
        case 2:
            if contador > 0:
                media_salarial = soma_salario / contador
                print("\n= Exibindo resultados =")
                print(f"A média salarial do grupo: {media_salarial}")
                print(f"A maior idade do grupo: {maior_idade}")
                print(f"A menor idade do grupo: {menor_idade}")
                print(f"A quantidade de mulhres com o salario acima de 5K: {mulheres5kk}")
            else:
                print("\nNão foram informados os dados necessários.")
            time.sleep(3)
            os.system("cls")
        case 3:
            print("\n Fim =")
            break
       
        