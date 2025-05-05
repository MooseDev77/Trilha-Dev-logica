from dataclasses import dataclass
import os
os.system("cls")
lista_autor=[]
QUANTIDADE_DE_LIVROS = 1
@dataclass
class Autor:
    nome:str
    biografia: str
    
@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor
    
def exibir_dados(self):
    print(f"Titulo: {self.titulo} | Autor: {self.Autor.nome} | | Ano: {self.ano}")

for i in range(QUANTIDADE_DE_LIVROS):
    informacao = Livro(
            titulo=str(input("Digite o nome o titulo: ")),
            ano=int(input("Digite o ano: ")),
            autor = Autor(
                nome=str(input("Digite o nome do Autor: ")),
                biografia=input("digite a biografia: "),
            )
)
lista_autor.append(Livro)

print("\n Salvando dados = ")
texto_arquivo = "dados.autor.txt"
with open (texto_arquivo, "a", encoding="utf-8") as arquivo_autor:
    for Livro in lista_autor:
        arquivo_autor.write(f"Titulo: {informacao.titulo} | Autor: {informacao.autor.nome} | | Ano: {informacao.ano}")

print("\n Dados salvos com sucesso = ")

#Exibindo dados do arquivo txt.
print("\n lendo dados do arquivo = ")

try:
    with open(texto_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(f"{linha.strip()}")
except FileNotFoundError:
    print("Arquivo não encontrado.")