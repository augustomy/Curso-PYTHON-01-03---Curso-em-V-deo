n = int(input('Digite um número \033[1;31minteiro\033[m: '))
if n % 2 == 0:
    print('O número {} informado é \033[1;34mpar\033[m!'.format(n))
else:
    print('O número {} é \033[1;35mímpar\033[m!'.format(n))