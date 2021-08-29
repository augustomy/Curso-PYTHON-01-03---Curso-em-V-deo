#Importando módulos(bibliotecas)
#Importa todos os dados de uma biblioteca: import "nome da biblioteca"
import math
x = float(input('Digite um número: '))
#raiz = math.sqrt(x)

#Importa apenas a função da biblioteca que será utilizada: from "nome da biblioteca" import "nome da função"
from math import sqrt
raiz = sqrt(x)

print('A raiz quadrada de {} vale {}.'.format(x, raiz))
