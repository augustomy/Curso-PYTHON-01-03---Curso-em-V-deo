nomec = input('Digite seu nome completo: ')
nome = nomec.strip()
ma = nome.upper()
mi = nome.lower()
seq = nome.split()
#MANEIRA 1 DE FAZER A CONTAGEM DE TODAS AS LETRAS EXCLUINDO OS ESPAÇOS
#aux = nome.replace(' ','') #SUBSTITUI OS ESPAÇOS POR NADA
#nomecompleto = len(aux) #REALIZA CONTAGEM DO NOME COMPLETO TODO JUNTO
#MANEIRA 2 DE FAZER A CONTAGEM DE TODAS AS LETRAS EXCLUINDO OS ESPAÇOS
nomecompleto = len(nome) - nome.count(' ')
primeironome = len(seq[0])
print('Nome com letras maiúsculas: {}\nNome com letras minúsculas: {}\nQuantidade de letras ao todo sem espaços: {}\nQuantidade de letras do primeiro nome: {}'.format(ma, mi, nomecompleto, primeironome))
