nome = input("Digite seu nome completo : ").strip().capitalize()
nome_formatado = nome.split()
print(f"seu primeiro nome é {nome_formatado[0]} \n e seu último nome é : {nome_formatado[-1]}")