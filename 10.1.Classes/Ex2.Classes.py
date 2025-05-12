import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class pessoa:
    nome: str
    email: str
    telefone: float
    endereco: str
    
pessoa0 = pessoa("Fernando", "nando@gma.com", 759907280 , "Rua,guanabara78")

print(f"Nome: {pessoa0.nome}\t| Email: {pessoa0.email}\t | telefone: {pessoa0.telefone}\t | Endereço: {pessoa0.endereco}.")

    