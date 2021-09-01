p = float(input('Digite o preço do produto: R$'))
d = p * 0.95
print('O valor do produto com \033[4;32mdesconto\033[m será de \033[1;32;40mR${:.2f}\033[m'.format(d))
