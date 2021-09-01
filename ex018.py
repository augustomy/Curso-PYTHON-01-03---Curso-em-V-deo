import math
a = float(input('Digite o valor de um ângulo em \033[1;41mgraus\033[m: '))
rad = math.radians(a)
s = math.sin(rad)
c = math.cos(rad)
t = math.tan(rad)
print('Ângulo digitado: {}°\nSeno: {:.3f}\nCosseno: {:.3f}\nTangente: {:.3f}'.format(a, s , c, t))