alugado = int(input("quantos dias o carro ficou alugado?"))
kilometragem = float(input("quantos kms foram rodados?"))
total = (60*alugado) + (0.15*kilometragem)
print(f"O valor total a pagar é : {total:.2f}")