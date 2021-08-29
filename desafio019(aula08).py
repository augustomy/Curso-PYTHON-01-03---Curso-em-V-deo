import random
a1 = (input('Digite o nome do primero aluno: '))
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
r = random.choice([a1, a2, a3, a4])
print('Alunos participantes: {} | {} | {} | {}\nAluno sorteado: {}'.format(a1, a2, a3, a4, r))
