continuar = ''
contador = media = soma = maior = menor = 0
while continuar!='N':
    numero = int(input("Digite um número: "))
    contador +=1
    soma+=numero
    if contador == 1:
        maior = numero
        menor = numero
    elif numero>maior:
        maior = numero
    elif numero<menor:
        menor = numero
    continuar = input("Quer continuar? [S/N] ").strip().upper()[0:1]
    while continuar not in ['S', 'N']:
            continuar = input("Opção inválida. Quer continuar? [S/N] ").strip().upper()[0:1]
media = soma/contador
print(f"Você digitou {contador} números e sua média é : {media}\n o maior valor foi {(maior)} e o mínimo foi : {menor}")