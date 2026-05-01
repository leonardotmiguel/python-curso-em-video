# Desafio 052
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        print('\33[33m', end='- ')
        tot += 1
    else:
        print('\33[31m', end='- ')
    print(f'{c} ', end='')
print('ACABOU')
print(f'\33[mO número {num} foi divisível {tot} vezes.')
if tot == 2:
    print('Por isso ele é número primo.')
else:
    print('Por isso ele não é número primo')