import os
os.system("cls")

def MPC (MT):
    return MT * 100;
print("= CONVERTER METROS PARA CENTÍMETROS =")
MT = float(input("Digite o numero aí namoral: "))
CM = MPC(MT)
print (f"\n= Resultado =")
print (f"{MT} metros é igual a {CM} centímetros.")

