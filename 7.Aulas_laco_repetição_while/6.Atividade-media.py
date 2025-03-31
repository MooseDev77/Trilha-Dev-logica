import os
os.system("cls")
nota = 0

while True:

    nota_1 = int(input("Digite sua primeira nota cidadao: "))
    nota_2 = int(input("Digite sua segunda nota cidadao: "))

    if nota_1 < 0 or nota_1 > 10:
        print("Digite sua primeira nota cidadao: \n")
    if nota_2 < 0 or nota_2 > 10:
        print("Digite sua segunda nota cidadao: \n")
    else:
        break    


media = (nota_1 + nota_2) /2
print (f"media: {media}")

