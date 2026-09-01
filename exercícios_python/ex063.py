numero = int(input("Escreva um número inteiro :  "))
valorA=0
valorB=1
contador = 0
temporario = 0
while contador !=numero:
    print(valorA, end=' ---> ')
    temporario = valorA+valorB
    valorA=valorB
    valorB=temporario
    contador += 1   
print("FIM")