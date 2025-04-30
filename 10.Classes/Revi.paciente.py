import os
from dataclasses import dataclass
os.system("clear")

@dataclass
class Paciente:
    #Atributos: são variáveis que pertencem o classe.
    nome: str
    idade: str
#Método: é uma função que pertence a classe.
#Este método para exibir dados do paciente.
    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade}\n\n")

#Atribuindo dados ao paciente1.
Paciente1 = Paciente(
 nome= input("Digite seu nome: "),
 idade= int(input("Digite a sua idade: "))
)                       


#Exibindo dados do paciente.
Paciente1.exibir_dados()