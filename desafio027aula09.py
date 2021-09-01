nomec = input('Digite o nome completo: ')
nome = nomec.strip() #elimina os espaços da esquerda (começo) e da direita (fim)
primeiro2 = nome.split()
primeiro = primeiro2[0]
ultimo2 = nome.rsplit()
ultimo = ultimo2[-1]
print('Primeiro nome: {}\nÚltimo nome: {}'.format(primeiro, ultimo))
