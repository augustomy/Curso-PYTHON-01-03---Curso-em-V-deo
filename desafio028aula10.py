import random
n = random.randint(0,5)
x = int(input('Digite seu palpite de 0 a 5: '))
if n == x:
    print('Parabéns, você acertou!\nO número escolhido foi {}.'.format(n))
else:
    print('Você errou.\nO número escolhido foi {}.'.format(n))
