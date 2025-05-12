from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class funcionario:
     nome: str
     nascimento: str
     rg: float
     cpf: float
 
     def exibir_dados_pessoais(self):
         print(f"Nome:{self.nome} \nNascimento:{self.nascimento} \nRG:{self.rg} \nCPF:{self.cpf} \n\n")
 
lista_funcionario = []
QUANTIDADE_funcionario = 1
 
for i in range(QUANTIDADE_funcionario):
     Funcionario = funcionario(
                 nome= str(input("Digite o seu nome: ")),
                 nascimento= str(input("Digite o seu Nascimento: ")),
                 rg= float(input("Digite o seu RG: ")),
                 cpf= float(input("Digite o seu CPf: "))
 
     )
 
     lista_funcionario.append(funcionario)
     print()
     
def arquivando_lista(funcionario):
    texto_funcionario = "Dados_dos_funcionarios.txt"
    with open (texto_funcionario, "a") as arquivo_do_funcionario:
            for funcionario in lista_funcionario:
                arquivo_do_funcionario.write(f"Nome:{funcionario.nome} \nNascimento:{funcionario.nascimento} \nRG:{funcionario.rg} \nCPF:{funcionario.cpf}")
    
    lista_funcionario.append(texto_funcionario)
print("Dados salvos com sucesso.")
print()
        
try:
    with open (texto_funcionario, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readline()
        for linhas in linhas:
            print(f"{linhas.strip()}")
except FileExistsError:
       print("Arquivo não encontrado")
                   
               
    
 
 
 
 
 
    print("\nExibindo Dados.")
for Livros in lista_funcionario:
     Livros.exibindo_dados_funcionario()