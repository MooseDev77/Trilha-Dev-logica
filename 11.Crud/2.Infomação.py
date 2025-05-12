import os
os.system("clear")
from dataclasses import dataclass
import time
lista_pessoas = []
QUANTIDADE_PESSOAS = 1

@dataclass
class informacao:
    nome:str
    nascimento:float
    cpf:float
    funcao:str

class exibindo_dados(lista_pessoas):
    print(f"""
          Nome:{lista_pessoas.nome}
          Data de Nascimento:{lista_pessoas.nascimento}
          cpf:{lista_pessoas.cpf}
          função:{lista_pessoas.funcao}              
          """)

def verificar_lista_vazia(lista_pessoas):
    if not lista_pessoas:
        return True
    return False

def adicionar_informacao(lista_pessoas):
    nome = input("Digite o nome que quer adicionar:")
    nascimento = float (input("Digite a data de nascimento:"))
    cpf = float (input("Digite o CPF:"))
    funcao = input("Digite a sua função:")
    adicionar_informacao.append()
    print(f"\n {nome} adicionado com sucesso.")
    print(f"\n {nascimento} adicionado com sucesso.")
    print(f"\n {cpf} adicionado com sucesso.")
    print(f"\n {funcao} adicionado com sucesso.")

def mostrar_informacao(lista_pessoas):
    if verificar_lista_vazia(lista_pessoas):
        print("\n A lista está vazia.")
        return

    print("\n - lista de informações - ")
    for exibindo_dados in lista_pessoas:
        print(f" - {exibindo_dados} - ")

def excluir_informacao(lista_pessoas):
    if verificar_lista_vazia(lista_pessoas):
        print("\n A lista está vazia.")
        return
    
    mostrar_informacao(lista_pessoas)
    nome_remover = input("Digite o nome que deseja remover:")
    if nome_remover in lista_pessoas:
        lista_pessoas.remove(nome_remover)
        print(f"{nome_remover} foi excluido da lista.")
    else:
        print(f" O nome {nome_remover} não foi encontrado na lista.")

def atualizar_informacao(lista_pessoas):
    if verificar_lista_vazia(lista_pessoas):
        print("\n A lista está vazia.")
        return
    
    mostrar_informacao(lista_pessoas)
    nome_antigo = input("Digite o nome que deseja atualizar: ")
    if nome_antigo in lista_pessoas:
        nome_novo = input(f"Digite o novo nome para {nome_antigo}:")
        indice = lista_pessoas.index(nome_antigo)
        lista_pessoas[indice] = nome_novo
        print(f"O nome antigo:{nome_antigo}, foi substituido pelo nome: {nome_novo}.")
    else:
        print(f"\n O {nome_antigo} não foi encontrado.")

while True:
    print("""
    - Gerenciador de nomes -
    1 - Adicionar
    2 - Listar nomes
    3 - Atualizar
    4 - Remover
    5 - Sair
    """)
    opcao = int(input("Digite uma das opções acima: "))

    match opcao:
        case 1:
            adicionar_informacao(lista_pessoas)
        case 2:
            mostrar_informacao(lista_pessoas)
        case 3:
            atualizar_informacao(lista_pessoas)
        case 4:
            excluir_informacao(lista_pessoas)
        case 5:
            print("\n Encerrando o programa. ")
            break
        case _:
            print("\nOpção inválida.\nTente novamente.")
    time.sleep(5)
    os.system("clear")






