import os
os. system("clear")


# Faça um programa que calcule o "peso ideial" de um usuário de acordo com um caractere identificador
# de sexo ("M") para Masculino ou "F" para feminimo) inserido pelo mesmo. A fórmula para cada um dos
# dois casos está definida abaixo.

# Caso "M", utilize a fórmula: (72.7 x altura) - 58
# Caso "F", utilize a fórmula: (62.1 x altura) - 44.7


genero = str (input("Digite se é Masculino ou Feminino: "))
altura = float(input("Digite sua altura: "))

match genero:
    case "M":
        peso_ideial = (72.7 * altura) -58
        print (f"Seu peso ideal é: {peso_ideial:.2f}")
    case "F":
        peso_ideial = (62.1 * altura) -44.7
        print (f"Seu peso ideal é {peso_ideial:.2f}")
    case _:
        print("Opção invalida")
    
    
