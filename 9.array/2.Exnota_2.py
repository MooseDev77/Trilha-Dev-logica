import os
os.system("clear")

lista_notas = []
QUANTIDADE_NOTAS = 3

for i in range(QUANTIDADE_NOTAS):
   nota = float(input("Digite a sua nota: "))
   lista_notas.append(nota)

media = sum(lista_notas) / QUANTIDADE_NOTAS

print(f"notas:{lista_notas}")
print(f"Media: {media}")
