import random
import time
print('\033[1;36m-o-\033[m' * 20)
print('\033[1;31mJogo\033[m \033[1;32mda\033[m \033[1;33madvinhação\033[m \033[1;34mV1.0\033[m')
print('\033[1;35m-o-\033[m' * 20)
n = int(input('Digite seu palpite de 0 a 5: '))
x = random.randint(0,5)
print('Processando...')
time.sleep(2)
if n == x:
    print('\033[1;32mParabéns! Você acertou o número escolhido:\033[m \033[4m{}\033[m'.format(x))
else:
    print('\033[1;31mQue pena! Você errou. O número escolhido foi\033[m \033[4m{}\033[m. Tente novamente.'.format(x))
