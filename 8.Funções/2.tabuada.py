import os
os.system("cls")

def tabuada(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")
              
print("=TABUADA =")
numero = int(input("Digite um número: ")) 
tabuada(numero)  
           