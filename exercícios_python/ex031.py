kilometragem = int(input("quantos kms você rodou?"))
if kilometragem>200:
    print(f"o valor da viagem foi : {kilometragem*0.45} reais")
else:
    print(f"o valor da viagem é : {kilometragem*0.50} reais")