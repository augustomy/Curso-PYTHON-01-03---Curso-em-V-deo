n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
if n1 >= n2 >= n3:
    print('Maior número: {}\nMenor número: {}'.format(n1, n3))
if n1 >= n3 >= n2:
    print('Maior número: {}\nMenor número: {}'.format(n1, n2))
if n2 >= n1 >= n3:
    print('Maior número: {}\nMenor número: {}'.format(n2, n3))
if n2 >= n3 >= n1:
    print('Maior número: {}\nMenor número: {}'.format(n2, n1))
if n3 >= n1 >= n2:
    print('Maior número: {}\nMenor número: {}'.format(n3, n2))
if n3 >= n2 >= n1:
    print('Maior número: {}\nMenor número: {}'.format(n3, n1))
