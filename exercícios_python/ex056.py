soma = 0
media = 0 
maior_idade = 0
contador_mulheres = 0
nome_maisVelho = ''
for i in range(1,5):
    nome = input("digite seu nome ").strip()
    idade = int(input("digite sua idade : "))
    sexo = input("digite seu sexo M/F ").upper().strip()
    soma += idade
    if sexo == "M":
        if idade>maior_idade:
            maior_idade = idade
            nome_maisVelho = nome
    if sexo == "F" and idade<20:
        contador_mulheres +=1
media = soma/4
print(f" a media das idades vai ser igual a : {media}")
print(f" o nome do homem mais velho é  {nome_maisVelho} e ele tem {maior_idade} anos")
print(f" a quantidade de mulheres com idade inferior a 20 anos é : {contador_mulheres}")