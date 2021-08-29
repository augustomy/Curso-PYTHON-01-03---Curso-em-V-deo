from math import sin, cos, tan, degrees, radians, trunc
x = float(input('Digite o valor de um ângulo em Graus: '))
rad = radians(x)
s = (sin(rad))
c = (cos(rad))
t = (tan(rad))
print('Seno de {}°: {:.3f}\nCosseno de {}°: {:.3f}\nTangente de {}°: {:.3f}'.format(x, s, x, c, x, t))
