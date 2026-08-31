sexo = input("Digite seu sexo M/F : \n").upper().strip()[0]
while sexo != 'M' and  sexo != 'F':
    sexo = input("Digite seu sexo M/F : \n").upper().strip()[0]
    print("Dado inválido. Por favor digite seu sexo corretamente.")
print(f" O Sexo {sexo} cadastrado com sucesso!")
