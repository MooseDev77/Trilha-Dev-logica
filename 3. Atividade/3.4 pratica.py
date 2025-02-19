#Limpar o terminal.
import os 
os.system ("clear")
#dê 3 notas de um aluno, some e tire a média dele. se a nota for >= a 7, então: aprovado, se não: reprove

Nota_1 =  float(input("digite a sua pirmeira nota:"))
Nota_2 =  float(input("digite a sua segunda nota:"))
Nota_3 =  float(input("digite a sua terceira nota:"))

soma = Nota_1 + Nota_2 + Nota_3
media = soma/ 3

print(f"media: {media}")

if media < 7: 
    print ("Reprovado")

else:
    print ("Aprovado")



    



   