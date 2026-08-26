velocidade = int(input("Diga a velocidade do carro em km/h\n"))
multa = (velocidade - 80)*7
if velocidade>80:
    print(f"Você exerceu a velocidade limite! sua multa é de : {multa} Reais")
else:
    print("Você passou dentro do limite de velocidade. Dirija com cuidado!")