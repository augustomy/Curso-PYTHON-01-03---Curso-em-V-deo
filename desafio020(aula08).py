import random
a1 = (input('Digite o nome do primero aluno: '))
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
o = random.sample([a1, a2, a3, a4], k=4)
print('Ordem de apresentação dos trabalhos:\n{}'.format(o))