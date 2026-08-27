import datetime
dia_atual = datetime.date.today()
ano_atual = dia_atual.year
ano = int(input("diga um ano qualquer. Digite 0(zero) para analisar o ano atual\n"))
if ano == 0:
    ano = ano_atual

if ( ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0 :
    print(f" o ano {ano} é bissexto!")

else:
    print(f"o ano {ano} não é um ano bissexto")