numero = 0
soma = 0
contador = 0
numero = int(input("Escreva um número(999 para parar) "))
while numero!=999:
    soma+=numero
    contador+=1
    numero = int(input("Escreva um número(999 para parar) "))
print(f"você digitou {contador} números e a soma deles é : {soma}")
