import datetime
ano = int(input('Digite o ano para saber se ele é Bissexto ou digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[1;32mO ano\033[m \033[4;34m{}\033[m \033[1;32minformado é Bissexto!\033[m'.format(ano))
else:
    print('\033[1;31mO ano\033[m \033[4;34m{}\033[m \033[1;31minformado não é Bissexto!\033[m'.format(ano))
