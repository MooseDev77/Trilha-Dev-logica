import os
os.system("cls")

def inflacionar (preco):
    if preco < 100:
        resultado = preco *1.10 #Inflacionar 10%
    if preco >= 100:
        resultado = preco *1.20 #Inflacionar 20%
        return resultado
def descontar (preco):
    if preco < 100:
        resultado = preco *0.10 #descontar 10%
    if preco >= 100:
        resultado = preco *0.20 #descontar 20%
        return resultado

preco_produto = float(input("Digite a quantia do pagamento: "))
preco_inflacionado = inflacionar(preco_produto)
preco_descontado = descontar(preco_produto)

print(f"Preço final inflacionado: {preco_inflacionado:.2f}")
print(f"Valoe do desconto: {preco_descontado:.2f}")