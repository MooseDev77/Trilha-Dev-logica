import os 
import time
os.system("clear ||cls")

numero = int(input("Digite o numero que deseja: "))

print("contagem regressiva")
for i in range(numero,0,-1):
    print(f"A bomba vai explodir: {i}")
    time.sleep(0.01)

print("BOOOM!")    
