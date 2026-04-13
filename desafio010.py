# Desafio 010
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$ 1,00 = 3,27

n = float(input('Quantos reais você tem? '))
print(f'No montante de R$ {n}\nVocê tem em dólares o total de US$ {n / 3.27:.2f}')