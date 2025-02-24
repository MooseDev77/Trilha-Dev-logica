#Elabore um algoritmo para solicitar ao usuário o login e a senha.
#Considere que os dados do usuário já estão cadastrados.
#caso o login e senha estejam corretos, mostre a mensagem:
#"bem-vindo!"
#Caso contrário, mostre a mensagem:
#Login ou senha inválidos."

login_cadastrado = "Moose"
senha_cadastradas = "123"


login = input("digite o login:")
senha = input("digite sua senha:")

if login == login_cadastrado and senha == senha_cadastradas:
    print("bem vindo")
else:
    print("login ou senha inválidos!")