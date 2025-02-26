import os 
os.system("clear")

#Faça um algoritmo que colicite ao usuário dois número
# e um caractere que calcula as operações basicas 
# e um caractere que calcula as operações basicas 




#Entrda
primeiro_numero =  int(input("digite um número:"))
operador = input("digite a operação que deseja (+ - * /): ")
segundo_numero = int(input("digite um número: "))

#processamento
match operador:
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-":
        resultado = primeiro_numero - segundo_numero
    case "*":
        resultado = primeiro_numero * segundo_numero
    case "/":
        resultado = primeiro_numero / segundo_numero
    case _:
        resultado = "Opção inválida."

#Saída        
print(f"primeiro número: {primeiro_numero}")
print(f"Opereção: {operador}")
print(f"segunda número: {segundo_numero}")
print(f"Resultado: {resultado}")