import os 
import time
os.system("clear ||cls")

numero = int(input("Digite o numero que deseja: "))

print("soltando")
for i in range(numero,121,2):
    print(f"Ir além: {i}")
    time.sleep(0.1)

print("contando")    
