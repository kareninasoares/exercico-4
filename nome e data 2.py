import datetime

n = str(input('digite seu nome:')).strip()
nome = n.split()
print(n.capitalize())
ano = eval(input('nasceu em que ano:'))
mes = eval(input('nasceu em que mês:'))
dia = eval(input('nasceu em que dia:'))
date = ('ano = 2000, mês = 10, dia = 15')
txt = (input('Pedro nasceu no dia:'))
print(txt . format(datetime.date(2000,10,15)))

