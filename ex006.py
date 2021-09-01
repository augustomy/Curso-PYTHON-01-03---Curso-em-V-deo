x = float(input('Digite um número: '))
d = x * 2
t = x * 3
r = x ** 0.5
# r = pow(x, 0.5)
print('O dobro de \033[7m{}\033[m é \033[1;32m{}\033[m.\nO triplo de \033[7m{}\033[m é \033[1;32m{}\033[m.\nA raiz quadrada de \033[7m{}\033[m é \033[1;32m{}\033[m.'.format(x, d, x, t, x, r))
