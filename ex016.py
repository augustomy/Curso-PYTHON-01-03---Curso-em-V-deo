import math
x = float(input('Digite um número: '))
i = math.trunc(x)
print('O número digitado foi {} e possui \033[4;36mparte\033[m \033[4;36minteira\033[m \033[4;32m{}\033[m.'.format(x,i))
