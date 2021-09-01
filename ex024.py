#nomecidade = input('Digite sua cidade: ')
#nsemespacos = nomecidade.strip() #ELIMINA OS ESPAÇOS DA ESQUERDA (COMEÇO) E DA DIREITA (FINAL)
#nupper = nsemespacos.upper() #PADRONIZA A CIDADE EM LETRAS TODAS MAIÚSCULAS
#aux = nupper.split() #SEPARA AS PALAVRAS (EM CASO DE PALAVRAS COMPOSTAS)
#resultado = 'SANTO' in aux[0] #PROCURA A PALAVRA SANTO NO PRIMEIRO ELEMENTRO DA SEQUENCIA aux
#print(resultado)

#OUTRA FORMA
nomecidade = input('Digite sua cidade: ')
nsemespacos = nomecidade.strip() #ELIMINA OS ESPAÇOS DA ESQUERDA (COMEÇO) E DA DIREITA (FINAL)
nupper = nsemespacos.upper() #PADRONIZA A CIDADE EM LETRAS TODAS MAIÚSCULAS
print('Sua cidade possui Santo como primeiro nome? {}'.format(nupper[0:5] == 'SANTO'))
