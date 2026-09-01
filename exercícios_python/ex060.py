#Versão com FOR
numero = int(input('digite o número para calcular o fatorial : '))
acumulador = 1 
for i in range(numero, 0, -1):
    print(i, end='x' if i>1 else'=')
    acumulador*=i
print(acumulador)
#Versão com WHILE
'''numero = int(input("Digite um número para calcular o fatorial : "))
acumulador = 1
while numero != 0:
    print(numero, end= "x" if numero>1 else "=")
    acumulador*=numero
    numero -= 1
print(acumulador)'''
