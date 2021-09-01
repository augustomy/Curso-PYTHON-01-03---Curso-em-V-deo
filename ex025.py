x = input('Digite seu nome completo: ')
nomesemespacos = x.strip()
nomeupper = nomesemespacos.upper()
resultado = 'SILVA' in nomeupper
print('Seu nome tem Silva? {}'.format(resultado))
