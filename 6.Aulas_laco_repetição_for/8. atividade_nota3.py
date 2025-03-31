import os 

os.system("clear ||cls")

soma = 0
print("solicitando números")
for i in range(3):
    numero = int(input(f"Suas notas cidadão: "))
    soma += numero
    media =   soma/3

if media >= 7:
        print ("Aprovado")
elif media < 4:
        print ("Reprovado")



print()
print(f"media: {media:.2f}")

        



   