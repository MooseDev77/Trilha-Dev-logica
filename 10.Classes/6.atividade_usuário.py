import os
from dataclasses import dataclass
os.system("clear")

@dataclass
class usuario:
    nome: str
    idade: str
    peso: float
    altura: float

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade} \nPeso: {self.peso} \nAltura:{self.altura}")

lista_de_usuarios = []
QUANTIDADE_USUARIO = 2

for i in range(QUANTIDADE_USUARIO):
    usuario1 = usuario(
        nome = str (input("Digite o seu nome: ")),
        idade = int(input("DIgite sua idade: ")),
        peso = float(input("Digite seu peso: ")),
        altura = float(input("Digite a sua altura: "))
        
                                                         )

    lista_de_usuarios.append(usuario1)
    print()

print("\nExibindo os dados dos usuários...")
for usuario1 in lista_de_usuarios:
    usuario1.exibir_dados()