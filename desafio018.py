# Desafio 018
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(an))
print(f'O ângulo tem o seno de {seno:.2f}')
cosseno = cos(radians(an))
print(f'O ângulo tem o cosseno de {cosseno:.2f}')
tangente = tan(radians(an))
print(f'O ângulo tem a tangente de {tangente:.2f}')