velocidade = float(input('Digite a velocidade em km/h: '))
if velocidade > 80:
    multa = 7 * (velocidade - 80)
    print('\033[7;33;41mVelocidade 80 km/h foi excedida!\033[m\n\033[1;33mVocê será multado(a) em\033[m \033[1;31mR${:.2f}\033[m\nTenha um ótimo dia!'.format(multa))
else:
    print('\033[1;32mVelocidade de acordo com o limite estipulado.\nTenha um ótimo dia!\033[m') 
