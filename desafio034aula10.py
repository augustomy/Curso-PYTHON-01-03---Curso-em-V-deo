salario = float(input('Digite o salaário do funcionário: R$'))
if salario > 1250.00:
    novo = salario * 1.10
    print('Salário informado: R${:.2f}\nNovo salário: R${:.2f}'.format(salario, novo))
else:
    novo = salario * 1.15
    print('Salário informado: R${:.2f}\nNovo salário: R${:.2f}'.format(salario, novo))
    