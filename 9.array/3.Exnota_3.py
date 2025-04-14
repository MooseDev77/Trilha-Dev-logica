import os
os.system("clear")


def calculo_media(lista_notas):
    
    media = sum(lista_notas) / QUANTIDADE_NOTAS
    return media
   

def situacao_notas(media):
    if media >= 7:
        resultado = "Situação: Aprovado."
    elif media >= 5:
        resultado = "Situação: Recuperação."
    else:
        resultado = "Situação: Reprovado."
        return resultado
    
lista_notas = []
QUANTIDADE_NOTAS = 4
    
for i in range (QUANTIDADE_NOTAS):
    nota = float(input("Digite suas notas: "))
    lista_notas.append (nota)

media = calculo_media(lista_notas)
resultado = situacao_notas (media)
    
print ()
for nota in lista_notas:
    print(nota)

print(f"Sua media é: {media:.2f}, vocé está: {resultado}")