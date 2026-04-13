# Desafio 012
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Digite o valor do produto: '))
n = p - (p * 5 / 100)
print(f'O valor de R$ {p} com 5% de desconto é de R$ {n:.2f}')