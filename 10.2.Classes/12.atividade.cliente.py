from dataclasses import dataclass
import os
os.system("clear")
QUANTIDADE_DE_FUNCIONARIO = 1
QUANTIDADE_DE_CLIENTE = 1
lista_funcionario = []
lista_cliente = []

@dataclass
class funcionario:
    nome: str
    admissao: float
    matricula: float
    endereco: str

@dataclass
class cliente:
    nome: str
    nascimento: float
    endereco: str

def exibindo_dados_funcionario(self):
    print(f"""Nome do funcionario: {self.funcionario.nome},
              Data de admissão: {self.funcionario.admissao},
              Matrícula: {self.funcionario.matricula},
              Endereço: {self.funcionario.endereco}""")
    
def exibindo_dados_cliente(self):
    print(f"""Nome do Cliente: {self.cliente.nome},
              Data de Nascimento: {self.cliente.nascimento},
              Endereço: {self.cliente.endereco}""")
    
for i in range(QUANTIDADE_DE_FUNCIONARIO):
  print (f"Digite o {i+1}° funcionario: ")
  informação_funcionario = funcionario(  
    nome = str(input("Digite o nome do funcionario: ")),
    admissao = float(input("Digite a data de admissão: ")),
    matricula = float(input("Digite a sua matricula: ")),
    endereco = str(input("Digite o seu endereço: ")) )
  lista_funcionario.append(funcionario)
os.system ("clear")

for i in range(QUANTIDADE_DE_CLIENTE):
  print (f"Digite o {i+1}° cliente: ")
  informação_cliente = cliente(  
    nome = str(input("Digite o nome do cliente: ")),
    nascimento= float(input("Digite o ano de nascimento: ")),
    endereco = str(input("Digite o seu endereço: ")) )
  lista_cliente.append(cliente)
os.system ("clear")

print("\n SALVANDO DADOS = ")
texto_arquivo_funcionario = "Dados.funcionario.txt"
with open(texto_arquivo_funcionario, "a", encoding="utf-8") as arquivo_funcionario:
   for funcionario in lista_funcionario:
      arquivo_funcionario.write(f"""
\n
Nome do funcionario:{informação_funcionario.nome}
Data de admissão:{informação_funcionario.admissao}
Matrícula:{informação_funcionario.matricula}
Endereço:{informação_funcionario.endereco}""")


texto_arquivo_cliente = "Dados.cliente.txt"
with open(texto_arquivo_cliente, "a", encoding="utf-8") as arquivo_cliente:
   for cliente in lista_cliente:
      arquivo_cliente.write(f"""
\n
Nome do cliente:{informação_cliente.nome}
Ano de nascimento:{informação_cliente.nascimento}
Endereço:{informação_cliente.endereco}""")

print("\n Dados salvos = ")
