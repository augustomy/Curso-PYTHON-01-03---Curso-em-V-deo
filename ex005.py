x = int(input('Digite um número \033[1;31minteiro\033[m: '))
a = x - 1
s = x + 1
print('O antecessor de \033[1;32m{}\033[m é \033[1;35m{}\033[m.\nO sucessor de \033[1;32m{}\033[m é \033[1;35m{}\033[m.'.format(x, a, x, s))
