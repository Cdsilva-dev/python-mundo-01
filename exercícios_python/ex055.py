maior = 0
menor = 0
for i in range(1,6):
    peso = float(input("digite seu peso : "))
    if i ==1:
        maior = peso
        menor = peso
    else:
        if peso>maior:
            maior = peso
        if peso<menor:
            menor = peso
    
print(f" o maior peso é {maior}\n o menor peso é {menor}")