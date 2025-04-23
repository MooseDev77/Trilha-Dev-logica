import os
os.system("clear")


QUANTIDADE_NUMEROS = 5
somar_positivos = 0
mostrar_negativos = 0 
lista_numeros = []

def processamento_P_N(numero):
    if numero >0:
        somar_positivos += numero
    elif numero <0:
         mostrar_negativos +=1
         return mostrar_negativos, somar_positivos
    
def pedindo_numeros():
    for i in range (QUANTIDADE_NUMEROS):
        numero = int(input(f"Digite os {i+1}° numero desejados: "))
        lista_numeros.append(numero)
    return lista_numeros

lista = pedindo_numeros()
somar_positivos, mostrar_negativos = processamento_P_N(lista_numeros)
    
print(f"\nNumeros negativos na lista:-{mostrar_negativos}")
print(f"Soma dos numeros positivos:{somar_positivos}")
