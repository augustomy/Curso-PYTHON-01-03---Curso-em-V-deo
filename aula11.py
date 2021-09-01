print('\033[7;37mOlá, Mundo!\033[m')

#SINTAXE PARA ESTILO, COR DA LETRA, COR DO FUNDO DA LETRA
#\003[E;C;Fm ->INÍCIO DE ONDE IRÁ SER APLICADO ESTILO, COR DA LETRA E COR DO FUNDO
#\003[m -> FINAL DE ONDE IRÁ SER APLICADO ESTILO, COR DA LETRA E COR DO FUNDO
#E: pode ser 0 (nenhum), 1 (negrito), 4 (sublinhado) ou 7 (negativo)
#C: pode ser de 30 a 37, onde cada valor possui uma cor diferente
#F: pode ser de 40 a 47, onde cada valor possui uma cor diferente
#OBS: em caso do estilo 7 (negativo) ser aplicado, a cor da letra será a cor do estilo e vice versa