n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Primeira nota: {}\nSegunda nota: {}'.format(n1, n2))
if m < 6:
    print('Sua média final é: {}\nInfelizmente você precisará fazer a prova substitutiva.'.format(m))
else:
    print('Sua média final é: {}\nVocê passou direto, parabéns!'.format(m))
