ano = int(input('Digite o ano: '))
if ano % 4 == 0:
    print('O ano informado foi {}.\nEle é bissexto.'.format(ano))
else:
    print('O ano informado foi {}.\nEle não é bissexto.'.format(ano))