soma = 0
for i in range(0,6):
    numero = int(input("Digite um número\n"))
    if numero % 2 == 0:
        soma += numero
print(f"a soma de todos os números pares é: {soma} ")