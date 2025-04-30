import os
from dataclasses import dataclass
os.system("clear")

@dataclass
class livros:
    nome: str
    autor: str
    categoria: str
    preco: float

    def exibir_dados_livros(self):
        print(f"Nome:{self.nome} \nAutor:{self.autor} \nCategoria:{self.categoria} \nPreço:{self.preco}\n\n")

lista_livros = []
QUANTIDADE_LIVROS = 1


for i in range(QUANTIDADE_LIVROS):
    Livros = livros(
                nome = str(input("Digite o nome do livro: ")),
                autor = str(input("Digite o nome do autor: ")),
                categoria= str(input("Digite o nome da categoria: ")),
                preco = float(input("Digite o valor do produto: "))  )

    lista_livros.append(Livros)
    print()

    nome_arquivo = "Dados_livros.txt"
    with open(nome_arquivo, "a") as arquivo_dos_livros:
        for Livros in lista_livros:
            arquivo_dos_livros.write(f"Nome:{Livros.nome} \nAutor:{Livros.autor} \nCategoria:{Livros.categoria} \nPreço:{Livros.preco}\n\n")

    print("Dados salvos com sucesso.")
    print()

    print("\nExibindo dados dos livros.")
for Livros in lista_livros:
    Livros.exibir_dados_livros()
