numero = int(input("digite um número : "))
contador_numPrimo = 0
for i in range(1, numero+1):
    print(i)
    if numero % i == 0:
        contador_numPrimo += 1
print(f"o número {numero} foi divisível {contador_numPrimo} vezes")
if contador_numPrimo == 2 :
    print(f"e por isso o número {numero} é primo")
else:
    print(f" e por isso o número {numero} não é primo")