frase = str(input('Digite uma frase: '))
qtd = frase.count('A') #conta quantas letras A a frase digitada possui
primeira = frase.find('A')
ultima = frase.rfind('A')
print('Quantidade de letras A: {}'.format(qtd))
print('Posição da primeira letra A: {}'.format(primeira))
print('Posição da última letra A: {}'.format(ultima))
