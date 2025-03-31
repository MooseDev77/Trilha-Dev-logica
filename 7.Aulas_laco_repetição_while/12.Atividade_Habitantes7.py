import os
os.system

print ("""
       
    CÓDIGO | DESCRIÇÃO
       1     ADICIONAR PESSOA
       2     EXIBIR RESULTADOS
       3     SAIR   
       
       """)
opcao = int (input("Digite 1 | 2 | 3 para a opção escolhida: "))

match opcao:
    case "1":
        idade = int(input("Informe a sua idade: "))
        sexo = input("Informe seu sexo (M/F): ").strip().upper()
        salario = float(input("Informe seu salario, por favor: "))
        dados.append({"idade": idadem, "sexo": sexo, "salario": salario})

    case "2":
        if not dados:
            print("Nenhum dado cadastrado. ")

        total_salario = sum(p["salario"] for p in dados)
        media_salario = total_salario / len(dados)
        
        idades = [p["idade"] for p in dados]
        maior_idade = max(idade)
        menor_idade = min(idade)

        mulheres5kk = sum(1 for p in dados if p["sexo"] == "f" and p["salario"] >= 5000.00)
        print(f"Média salario do grupo: R${media_salario:.2f}")
        print(f"Maior idade: {maior_idade, Menor_idade:} {menor_idade}")
        print(f"Quantidade de mulhres com salario a partir de R$5000.00: {mulheres5kk}")

  
        case_
        print("opçao inválida, tente novamente.")
    