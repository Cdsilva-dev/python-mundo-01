numero = 0
valor = int(input("digite um número "))
valor2 = int(input("digite outro número "))
while numero != 5:
    print("-"*50)
    print("Escolha uma das opções")
    numero = int(input(("[1] Somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n")))
    print("-"*50)
    if numero == 1:
        print(f"A soma dos valores {valor} e {valor2} é : {valor+valor2}")
    elif numero == 2:
        print(f"a multiplicação dos números {valor} e {valor2} é : {valor*valor2}")
    elif numero == 3:
        if valor2 != valor:
             print(f"o maior número é {max(valor, valor2)} e o menor é {min(valor, valor2)}")
        if valor == valor2:
            print("são iguais")
    elif numero == 4:
        print("Digite os novos números : \n")
        valor = int(input("digite o novo número "))
        valor2 = int(input("digite o segundo novo número "))
    elif numero == 5 :
        print("Finalizando programa...")
    else:
        print("Digite uma opção válida! Tente novamente : ")
