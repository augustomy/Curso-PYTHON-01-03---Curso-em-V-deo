l = float(input('Digite a largura da parede em \033[33mmetros\033[m: '))
a = float(input('Digite a altura da parede em metros: '))
s= l * a
t = s / 2
print('A parede informada ({}m x {}m) possui área de {:.2f}m².\nPara pintar essa parede, você precisará de \033[4;32m{:.2f}\033[m \033[4;32mlitros\033[m de tinta.'.format(l, a, s, t))
