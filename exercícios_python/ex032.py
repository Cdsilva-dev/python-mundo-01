import datetime
dia_atual = datetime.date.today()
ano_atual = dia_atual.year
#print(f"o ano atual é {ano_atual}")
ano = int(input("diga um ano qualquer\n"))
if (ano%4 and ano//100 != 0) or ano//400 :
    print(" é um ano bissexto")
else:
    print("não é um ano bissexto")