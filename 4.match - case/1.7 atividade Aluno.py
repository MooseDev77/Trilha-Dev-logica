import os
os. system("clear")

nome = str(input("Digite o seu nome: "))
Nota_1 = float(input("Digite sua primeira nota: "))
Nota_2 = float(input("Digite sua segunda nota: "))

media = (Nota_1 + Nota_2) / 2

print(f"Seu nome é: {nome}")
print(f"Nota 1: {Nota_1}")
print(f"Nota 2: {Nota_2}")             
print(f"media: {media}")      

if media >= 9:
    Conceito =  "A"
elif media > 7.5:
    Conceito = "b"
elif media >= 6:
    Conceito = "C"
elif media >= 4:
    Conceito = "D"
else:
    Conceito = "E"


match Conceito: 
    case "A" | "B" | "C":
        print(f"Conceito: {Conceito}")
        print("Aprovado.")
    case "D" | "E":
        print(f"Conceito: {Conceito}")
        print("Reprovado.")
    case _:
        print("Opção inválida.")        


  