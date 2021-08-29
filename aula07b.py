#Outra forma, utilizando apenas um print
x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo número: '))
s = x + y
m = x - y
v = x * y
d = x / y
p = x ** y
di = x // y
r = x % y
print('{} + {} = {}\n{} - {} = {}\n{} vezes {}: {}\n{} dividido por {}: {}\n{} elevado a potência {}: {}\n{} dividido inteiramente por {}: {} com resto {}'.format(x, y, s, x, y, m, x, y, v, x, y, d, x, y, p, x, y, di, r))
