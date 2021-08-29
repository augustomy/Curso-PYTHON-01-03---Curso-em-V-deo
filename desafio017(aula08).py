from math import sqrt
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = sqrt((co**2) + (ca**2))
print('Cateto oposto: {}\nCateto adjacente: {}\nHipotenusa: {}'.format(co, ca, h))
