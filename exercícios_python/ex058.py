import random
numero = random.randint(0,10)
resposta = 11
contador = 0
print("advinhe um número entre 0 a 10\n")
while resposta != numero:
    resposta = int(input("digite seu palpite\n"))
    contador +=  1
    if resposta>numero:
        print("menos... tente outra vez\n")
    elif resposta<numero:
        print("mais... tente outra vez\n")
print(f"Parabéns, você acertou! o número era : {numero} e a quantidade de tentativas que você precisou foi : {contador}")