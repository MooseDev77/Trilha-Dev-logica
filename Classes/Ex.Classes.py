import os 
from dataclasses import dataclass
os.system("cls")

@dataclass
class Pessoa:
    nome: str
    idade: int
    
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)
    
@dataclass
class Pet:
    nome: str
    idade: int
    raca:str
    
pet1 = Pet("Toto", 4, "pastor-alemão")
pet2 = Pet("Hulk", 6, "pitbull")



print(f"Nome do Pet 1: {pessoa1.nome}, Idade: {pessoa1.idade}") 
print(f"Nome: {pessoa2.nome}, Idade: {pessoa2.idade}")

print(f"Nome do Pet 2: {pet1.nome}, idade: {pet1.idade}, raça: {pet1.raca} ")
print(f"Nome: {pet2.nome}, idade: {pet2.idade}, raça: {pet2.raca}")          