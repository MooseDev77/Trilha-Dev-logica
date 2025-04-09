import os
os.system


def calculo_imc (peso,altura):
    somar = peso / (altura * altura)
    if somar <18.5:
        print("Abaixo do peso\nConsulte um nutricionista para orientação.")
    elif somar >= 18.5 < 24.9:
        print("Peso normal\nMantenha hábitos saudáveis.")
    if somar >= 25 <29.9:
        print("Sobrepeso\nConsidere uma dieta balanceada e atividade fisica.")
    elif somar >= 30 <34.9:
        print("Obsidade grau 1\nProcure orientação de um profissional de saúde.")
    if somar >= 35 <39.9:
        print("Obesidade gra 2\nColsulteum médico para avaliação e orientação.")
        
peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))


soma, subtrair = calculo_imc(peso, altura)

print(f"Seu IMC: {calculo_imc}")

