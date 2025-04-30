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

#Criando uma lista.
lista_de_pacientes = []
QUANTIDADE_PACIENTE = 4

#Atribuindo dados ao paciente1.
for i in range(QUANTIDADE_PACIENTE):
    Paciente1 = Paciente(
                    nome= input("Digite seu nome: "),
                    idade= int(input("Digite a sua idade: "))
                 )
                    
                    
                                           
    lista_de_pacientes.append(Paciente)

#Exibindo dados do paciente.
print("znExibindo dados do usuário.")
for Paciente in lista_de_pacientes:
    Paciente.exibir_dados()
