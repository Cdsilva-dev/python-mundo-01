segmento1 = float(input("primeiro segmento "))
segmento2 = float(input("segundo segmento "))
segmento3 = float(input("terceiro segmento "))
a,b,c = sorted([segmento1, segmento2, segmento3])
if a + b > c:
    print("forma um triângulo")
else:
    print("não forma um triãngulo")