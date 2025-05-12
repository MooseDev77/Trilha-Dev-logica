import os
from dataclasses import dataclass
os.system("clear")

@dataclass
class endereco:
    locradouro: str
    numero: int
    cidade: str

@dataclass
class pessoa:
    nome: str
    email: str
    endereco: endereco

nome = input("Digite o seu Nome: ")
email = input("Digite o seu Email: ")
numero_cs = input("Digite o número da casa: ")
cidade = input("Digite a sua cidade: ")
locradouro = input("Digite o seu locradouro: ")

def exibindo_dados(self):
    print(f"\tNome: {self.nome}, \tEmail: {self.email}\
            \tNúmero da casa: {self.endereco.numero_cs}, \tcidade: {self.endereco.cidade}\
            \tlocradouro: {self.endereco.locradouro}.")
    

endereco1 = endereco(locradouro, cidade, numero_cs)
pessoa1 = pessoa(nome, email, endereco1)

print("\nDados da pessoas: ")
pessoa1.exibindo_dados()



    