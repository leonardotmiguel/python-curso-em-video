# Desafio 013
# Faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Digite o valor do seu salário: '))
novo = s + (s * 15 / 100)
print(f'O salário de RS {s:.2f} reajustado com 15% de aumento será de R$ {novo:.2f}')