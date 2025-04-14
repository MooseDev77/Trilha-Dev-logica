import os 
os.system("clear")

def saudacao(paramento):
    print(f"Olá, {paramento}! Bem-vindo(a) oa nosso site.")

nome_visitante = input("digite o seu nome: ")
saudacao(nome_visitante)