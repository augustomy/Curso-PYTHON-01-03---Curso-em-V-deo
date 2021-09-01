import math
co = float(input('Digite o valor do cateto \033[1;31moposto\033[m: '))
ca = float(input('Digite o valor do cateto \033[1;32mdjacente\033[m: '))
h = math.sqrt((co ** 2) + (ca ** 2))
print('\033[1;31mCateto oposto: {}\033[m\n\033[1;32mCateto adjacente: {}\033[m\n\033[1;35mHipotenusa: {}\033[m'.format(co, ca, h))
