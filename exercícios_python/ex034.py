salario = float(input("Qual seu sálario?"))
if salario <= 1250:
    salario = salario +(salario*0.15)
    print(f"seu salário é :  {salario}")
else:
    salario = salario + (salario*0.10)
    print(f"seu salário é: {salario} ")