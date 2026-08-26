cidade = input("em que cidade você nasceu?").strip()
cidada_formatada = cidade.split()
if cidada_formatada[0].capitalize() == 'Santo':
    print(True)
else:
    print(False)