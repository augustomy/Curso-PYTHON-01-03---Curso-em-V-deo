km = float(input('Digite a distância da viagem em km: '))
if km <= 200:
    passagem = 0.5 * km
    print('Distância informada: {} km\nValor da passagem: R${:.2f}'.format(km, passagem))
else:
    passagem = 0.45 * km
    print('Distância informada: {} km\nValor da passagem: R${:.2f}'.format(km, passagem))
    