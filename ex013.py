s = float(input('Digite seu salário \033[4;33matual\033[m: R$'))
r = s * 1.15
print('Com o reajuste aplicado, seu salário de \033[4;33mR${:.2f}\033[m irá para \033[4;32mR${:.2f}\033[m'.format(s, r))