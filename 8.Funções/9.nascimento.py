import os
from datetime import date
os.system("cls")
def calcular (nascimento):
    resultado = date.today().year - nascimento
    return resultado

nascimento_usuario = int (input("Informe seu ano de nascimento: "))
resultado = calcular (nascimento_usuario)


print(f"A resultado da sua idade é: {resultado}")

