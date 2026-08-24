from math import hypot
cateto_oposto = float(input("Digite o valor do cateto oposto "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente "))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f"a hipotenusa vale :{hipotenusa}")

#Segunda forma de fazer :
#cateto_oposto = float(input("Digite o valor do cateto oposto"))
#cateto_adjacente = float(input("Digite o valor do cateto adjacente"))
#hipotenusa = (cateto_adjacente**2 + cateto_oposto**2) **(1/2)
#print(f"a hipotenusa vale :{hipotenusa}")