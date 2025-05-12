import os
from dataclasses import dataclass
os.system("clear")

@dataclass
class cidadao:
    nome: str
    nascimento: str
    rg: float
    cpf: float

    def exibir_dados_pessoais(self):
        print(f"Nome:{self.nome} \nNascimento:{self.nascimento} \nRG:{self.rg} \nCPF:{self.cpf} \n\n")

lista_cidadao = []
QUANTIDADE_CIDADAO = 2

for i in range(QUANTIDADE_CIDADAO):
    Cidadao = cidadao(
                nome= str(input("Digite o seu nome: ")),
                nascimento= str(input("Digite o seu Nascimento: ")),
                rg= float(input("Digite o seu RG: ")),
                cpf= float(input("Digite o seu CPf: "))

    )

    lista_cidadao.append(Cidadao)
    print()

    nome_arquivo = "Dados_Cidadão.txt"
    with open(nome_arquivo, "a") as arquivo_do_cidadao:
        for Cidadao in lista_cidadao:
            arquivo_do_cidadao.write(f"Nome:{Cidadao.nome} \nNascimento:{Cidadao.nascimento} \nRG:{Cidadao.rg} \nCPF:{Cidadao.cpf}")

    print("Dados salvos com sucesso.")
    print()

    print("\nExibindo Dados.")
for Livros in lista_cidadao:
    Livros.exibindo_dados_cidadao()
            