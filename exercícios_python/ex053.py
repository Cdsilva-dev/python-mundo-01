frase  = input("digite uma frase : ").strip().lower().replace(" ", "")
frase_invertida = frase[::-1]
print(f"o inverso de {frase} é  {frase_invertida}")
if frase == frase_invertida:
    print(f" e por isso é um palíndromo")
else:
    print(f"e por isso não é um palíndromo")

