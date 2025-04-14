import os
os.system("cls")

def calcular_imc(peso, altura):
    return peso / (altura * altura)

def situação (peso,altura):
    somar = peso / (altura * altura)
    if somar <18.5:
        classificacao = "Abaixo do peso"
        recomendacao = "Consulte um nutricionista para orientação."
    elif somar >= 18.5 < 24.9:
        classificacao = "Peso normal" 
        recomendacao = "Mantenha hábitos saudáveis."
    if somar >= 25 <29.9:
        classificacao = "Sobrepeso" 
        recomendacao = "Considere uma dieta balanceada e atividade fisica."
    elif somar >= 30 <34.9:
        classificacao = "Obsidade grau 1" 
        recomendacao = "Procure orientação de um profissional de saúde."
    if somar >= 35 <39.9:
        classificacao = "Obesidade gra 2" 
        recomendacao = "Colsulteum médico para avaliação e orientação."
    elif somar >40:
        classificacao = "Obsidade grau 3" 
        recomendacao = "Culsulte urgentemente um médico para avaliação."
    return classificacao, recomendacao

peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))


imc = calcular_imc(peso, altura)
classificacao, recomendacao = situação(imc)

print("\n= Exibindo resultados =")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")
print(f"Recomendação: {recomendacao}")


