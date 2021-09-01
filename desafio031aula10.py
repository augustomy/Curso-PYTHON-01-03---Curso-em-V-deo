dist = float(input('Digite a distância em km da viagem: '))
if dist <= 200:
    custo = 0.5 * dist
    print('Distância informada: {} km\nA passagem custará R${:.2f}'.format(dist, custo))
else:
    custo = 0.45 * dist
    print('Distância informada: {} km\nA passagem custará R${:.2f}'.format(dist, custo))
