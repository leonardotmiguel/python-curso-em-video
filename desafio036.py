# Desafio 036
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('=-=' * 10)
print('     EMPRÉSTIMO BANCÁRIO')
print('=-=' * 10)

casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do salário: '))
anos = int(input('Digite em quantos anos vai pagar: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R$ {casa:.2f} em {anos} anos ', end='')
print(f'a prestação será de R$ {prestacao:.2f}')
if prestacao <= minimo:
    print('Empréstimo CONCEDIDO')
else:
    print('Empréstimo NEGADO')