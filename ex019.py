import random
a1 = input('\033[1;31mPrimeiro aluno\033[m: ')
a2 = input('\033[1;32mSegundo aluno\033[m: ')
a3 = input('\033[1;33mTerceiro aluno\033[m: ')
a4 = input('\033[1;34mQuarto aluno\033[m: ')
s = random.choice([a1, a2, a3, a4])
print('Aluno sorteado: {}'.format(s))
