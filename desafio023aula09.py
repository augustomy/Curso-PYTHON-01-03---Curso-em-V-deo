#MANEIRA NÃO ESTÁ 100% CORRETA
#x = input('Digite um número inteiro de 0 a 9999: ')
#u = x[3]
#d = x[2]
#c = x[1]
#m = x[0]
#print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(u, d, c, m))


#MANEIRA 100% CORRETA
x = int(input('Digite um número de 0 a 9999: '))
m = x // 1000 % 10
c = x // 100 % 10
d = x // 10 % 10
u = x // 1 % 10 #DIVISÃO DE x POR 10 E PEGA O RESTO DESSA DIVISÃO
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(u, d , c, m))