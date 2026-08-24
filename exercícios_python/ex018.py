import math
angulo = float(input("Digite o valor do Ângulo desejado : "))
angulo_corrigido = math.radians(angulo)
print(f"o seno do ângulo de {angulo} é {math.sin(angulo_corrigido):.2f}")
print(f"o cosseno do ângulo de {angulo} é {math.cos(angulo_corrigido):.2f}")
print(f"a tangente do ângulo de {angulo} é {math.tan(angulo_corrigido):.2f}")