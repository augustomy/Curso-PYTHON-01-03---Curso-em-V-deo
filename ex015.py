km = float(input('Digite a quantidade de \033[1;32mkm rodados\033[m: '))
dias = float(input('Digite a quantidade de \033[1;34mdias pelos quais o carro foi alugado\033[m: '))
preço = (km * 0.15) + (dias * 60)
print('O valor a ser pago por \033[1;32m{} km rodados\033[m e \033[1;34m{} dias alugados\033[m será de:\n\033[1;35mR${:.2f}\033[m'.format(km, dias, preço))
