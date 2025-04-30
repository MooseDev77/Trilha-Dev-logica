import os
from dataclasses import dataclass
os.system("clear")

@dataclass
class Paciente:
    #Atributos: são variáveis que pertencem o classe.
    nome: str
    idade: int
#Método: é uma função que pertence a classe.
#Este método para exibir dados do paciente.
    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade}\n\n")

#Criando uma lista.
lista_de_pacientes = []
QUANTIDADE_PACIENTE = 2

#Atribuindo dados ao paciente1.
for i in range(QUANTIDADE_PACIENTE):
    paciente = Paciente(
                    nome= input("Digite seu nome: "),
                    idade= int(input("Digite a sua idade: "))
                 )
                    
                    
                                           
    lista_de_pacientes.append(paciente)
    print()

#salvando em um arquivo com .txt
nome_arquivo = "Dados_paciente.txt"
with open(nome_arquivo, "a") as arquivo_do_paciente:
    for paciente in lista_de_pacientes:
        arquivo_do_paciente.write(f"{paciente.nome}, {paciente.idade}\n")

print("Dados salvos com sucesso.")

#Exibindo dados do paciente.
print("\nExibindo dados do usuário.")
for paciente in lista_de_pacientes:
    paciente.exibir_dados()
