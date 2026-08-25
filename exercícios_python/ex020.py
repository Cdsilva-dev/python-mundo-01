import random
Nome = input("Digite o Primeiro nome ")
Segundo_nome = input("Digite o Segundo nome ")
Terceiro_nome = input("Digite o Terceiro nome ")
Quarto_nome =input("Digite o Quarto nome ")
lista = [Nome, Segundo_nome, Terceiro_nome, Quarto_nome]
random.shuffle(lista)
print(f"A ordem de apresentação será : C{lista}")