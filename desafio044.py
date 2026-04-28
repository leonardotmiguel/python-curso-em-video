# Desafio 044
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

produto = float(input('Preço do produto: R$ '))
print('''Escolha sua forma de pagamento:
[ 1 ] À vista   (dinheiro)   - 10% de desconto
[ 2 ] À vista   (cartão)     - 5% de desconto
[ 3 ] Parcelado (2x)         - preço normal
[ 4 ] Parcelado (3x ou mais) - 20% de juros''')
opcao = int(input('Escolha sua opção: '))
if opcao == 1:
    total = produto - (produto * 10 / 100)
elif opcao == 2:
    total = produto - (produto * 5 / 100)
elif opcao == 3:
    total = produto
    parcela = total / 2
    print(f'Sua compra em 2x custará R${parcela:.2f} por mês.')
elif opcao == 4:
    total = produto + (produto * 20 / 100)
    totalparc = int(input('Em quantas vezes quer parcelar: '))
    parcela = total / totalparc
    print(f'Você parcelou em {totalparc}x, seu produto custará R${parcela:.2f} por mês.')
print(f'O produto custa R${produto:.2f}, ao final ele custará R${total:.2f}')