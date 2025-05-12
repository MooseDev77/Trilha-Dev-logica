import os
from dataclasses import dataclass
os.system("cls")


@dataclass
class Endereco:
    logradouro: str
    numero: str
    
@dataclass
class pessoa:
    #Atriputos da classe (variáveis que pertecencem a uma classe).
    nome: str
    email: str
    telefone: float
    endereco: Endereco #Classe endereço.
    
# Método da classe (função que pertence a uma classe).
def exibindo_dados(self):
    print(f"Nome:{self.nome} | Email:{self.email} \
            telefone: {self.telefone} | locradouro {self.endereco.logradouro} \
            Numero: {self.endereco.numero}")

nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
telefone = input("Digite seu telefone: ")
endereco = input("Digite o seu Endereço: ")

endereco1 = Endereco ("Rua A", "33" )
pessoa1 = pessoa(nome, email, telefone, endereco1)
pessoa1.exibindo_dados()

