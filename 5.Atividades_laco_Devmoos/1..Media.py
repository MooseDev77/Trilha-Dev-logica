import os
os.system("cls")
nota_1 = int(input("Digite sua primeira nota: "))
nota_2 = int(input("Digite sua segunda nota: "))

while True:
    if nota_1 < 0 or nota_1 > 10:
        print("Nota invalida, tente novamente! \n")
    if nota_2 < 0 or nota_2 > 10:
        print("Nota invalida, tente novamente! \n")
    else: 
        break    
media = (nota_1 + nota_2) /2
    
if media >= 7:
        Resultado = "Aprovado"
elif media >= 5:
        Resultado = "Recuperação" 
else:
        Resultado = "Reprovado" 
        
print (f"\nSua media é {media}")
print (f"E você se encontra: {Resultado}")
    
            