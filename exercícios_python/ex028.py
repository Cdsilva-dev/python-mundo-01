import random
numero_aleatorio = random.randint(0,5)
numero = int(input("Advinhe um número entre 0 e 5\n "))
if numero == numero_aleatorio:
    print("Parabéns! Você acertou!")
else:
    print(f"Que pena, você errou! eu pensei no número {numero_aleatorio}")