v = float(input('Digite a velocidade de um carro em km/h: '))
if v > 80:
    km = 7 * (v - 80)
    print('Velocidade informada: {} km/h\nLimite 80 km/h de velocidade excedido.\nVocê terá que pagar R$ {:.2f}'.format(v, km))
else:
    print('Velocidade informada: {} km/h\nLimite 80 km/h de velocidade não foi excedido.\nVocê não terá que pagar multa.'.format(v))
