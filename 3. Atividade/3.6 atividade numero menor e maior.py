# Elabore um algoritmo usando operaçôes lógicas para solicitar ao usuário 2 número e escrever:

import os
os.system ("clear")

Numero_um = int(input("Digite o primeiro numero:"))
Numero_dois = int(input("digite o segundo numero:"))


menor = min(Numero_um, Numero_dois)
maior = max(Numero_um, Numero_dois)

print (f"primeiro número é: {Numero_um}")
print (f"segundo número é: {Numero_dois}")

if Numero_um == Numero_dois:
    print("os número são iguais.")

else:
    print (f"Maior: {maior}")
    print (f"Menor: {menor}")
    