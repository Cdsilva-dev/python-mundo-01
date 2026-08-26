numero = int((input("digite um número")))
numero_unidade = numero//1 % 10
numero_dezena = numero//10 % 10
numero_centena = numero//100 % 10
numero_milhar = numero//1000 % 10
print(f"unidade : {numero_unidade}")
print(f"dezena : {numero_dezena}")
print(f"centena : {numero_centena}")
print(f"milhar : {numero_milhar}")