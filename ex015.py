km = float(input('Digite a quantidade de km rodados: '))
dias = float(input('Digite a quantidade de dias pelos quais o carro foi alugado: '))
preço = (km * 0.15) + (dias * 60)
print('O valor a ser pago por {} km rodados e {} dias alugados será de:\nR${:.2f}'.format(km, dias, preço))
