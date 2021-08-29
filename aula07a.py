#Operadores Aritméticos:
#soma: +
#subtração: -
#multiplicação: *
#divisão: /
#exponencial: **
#divisão inteira: //
#resto da divisão inteira: %

#Ordem de precedência (Ordem do que será resolvido)
#1: () parenteses, colchetes e chaves
#2: ** exponenciais
#3: *, /, //, % multiplicação, divisão, divisão inteira e resto da divisão inteira
#4: + e - soma e subtração
x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo número: '))
print('A soma entre {} e {} vale: {}'.format(x, y, x + y))
print('{} menos {} vale: {}'.format(x, y, x - y))
print ('{} multiplicado por {} vale: {}'.format(x, y, x * y))
print('{} dividido por {} vale: {:.3f}'.format(x, y, x/y)) #:.3f significa o número de casas decimais
print('{} elevado a potência {} vale: {}'.format(x, y, x ** y))
print('{} dividido por {} é igual a {} com resto {}'.format(x, y, x // y, x % y))
