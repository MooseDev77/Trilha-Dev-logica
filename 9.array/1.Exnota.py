import os
os.system("cls")

#Criando uma .
lista_notas = []

# Adicionando 3 notas em uma lista.
for i in range(3):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)

# Exibindo todos os valores em uma lista.
print()
for nota in lista_notas: #forEach
    print(nota)
