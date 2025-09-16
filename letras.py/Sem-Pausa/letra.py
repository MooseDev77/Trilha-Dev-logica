from rich import print
import time

# Letra da música
lines = [
   ("Não, não, não, não", 0.04), #1
   ("Pera aí, pera aí", 0.04), #2
   ("Tava com saudade de nós dois", 0.09), #3
   ("E uma vontade de querer se arrepender", 0.08), #4
   ("Sentir o gosto e o sabor que nós já foi", 0.09), #5
   ("Com uma pitada das fotos que eu apaguei", 0.09), #6
   ("Me perguntando do porquê tu me ligou", 0.08), #7
   ("Mesmo sabendo que eu nunca ia atender", 0.08), #8
   ("Quer frequentar os lugares que eu sempre vou", 0.09), #9
   ("Com a esperança de um dia me rever", 0.08), #10
   ("To fodendo com as louca que dia tu xingou", 0.08), #11
   ("As que eu não conhecia, mas você fez eu querer", 0.08), #12
   ("Fala pra mim se é do jeito que imaginou", 0.08), #13
   ("E é assim que eu viveria no dia que me perder", 0.08), #14
]

def exibir_letra(lines):
    for texto, delay in lines:
        for letra in texto:
            print(f"[bold cyan]{letra}[/bold cyan]", end="", flush=True)
            time.sleep(delay)
        print()  # Quebra de linha ao final de cada verso

exibir_letra(lines)

