import os
os.system ("cls")

def calcular_media(nota_1, nota_2):
    soma = nota_1 + nota_2
    resultado = soma /2
    return resultado

def conferir_resultado(media):
  if media  >= 7:
    print(f"Aprovado!")
  else:
    print(f"Reprovado!")

print("=NOTAS =")
nota_1 = float(input("Digite sua nota: "))
nota_2 = float(input("Digite sua nota: "))
media = calcular_media(nota_1, nota_2)
conferir_resultado(media)
            
