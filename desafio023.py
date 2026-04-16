# Desafio 023
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Digite um número: 1834, unidade: 4 - dezena: 3 - centena: 8 - milhar: 1

numero = int(input('Digite um número qualquer: '))
n = str(numero)
print(f'Analisando o número {numero}')
print(f'Unidade: {n[3]} ')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')