x = input('Digite seu nome completo: ')
nomesemespacos = x.strip()
aux = nomesemespacos.split()
primeironome = aux[0]
aux2 = nomesemespacos.rsplit()
ultimonome = aux2[-1]
print('Seu primeiro nome é: {}\nSeu último nome é: {}'.format(primeironome, ultimonome))
