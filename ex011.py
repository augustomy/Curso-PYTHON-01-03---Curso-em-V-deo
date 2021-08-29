l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))
s= l * a
t = s / 2
print('A parede informada ({}m x {}m) possui área de {:.2f}m².\nPara pintar essa parede, você precisará de {:.2f}l de tinta.'.format(l, a, s, t))
