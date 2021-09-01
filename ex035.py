a = float(input('Reta 01: '))
b = float(input('Reta 02: '))
c = float(input('Reta 03: '))
if abs(b-c) < a < b+c and abs(a-c) < b < a+c and abs(a-b) < c < a+b:
    print('\033[1;32mSim, é possível formar um triângulo com as dimensões informadas:\033[m {}, {}, {}'.format(a, b, c))
else:
    print('\033[1;31mNão é possível formar um triângulo com as dimensões informadas:\033[m {}, {}, {}'.format(a, b, c))
    