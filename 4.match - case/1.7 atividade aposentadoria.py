import os
os. system("clear || cls")

matricula = int (input("digite o seu codigo: "))
Nascimento = int (input("Digite seu ano: "))
inicio_trab = int (input("Digite o ano que iniciou: "))
tempo_trab = int (input("Digite o tempo de trabalho: "))

idade = 2025 - Nascimento

if Nascimento >= 65 or tempo_trab >= 30:
    resultado = "requerer aposentadoria."
else:
    resultado = " Não Requerer aposentadoria."

print(f"\nMatricula: {matricula}")
print(f"idade: {idade}")
print(f"tempo de trabalho: {tempo_trab}")
print(f"Resultado: {resultado}")

