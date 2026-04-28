# Desafio 045
# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
print('=-=' * 10)
print('        JOGO DE JOKENPÔ')
print('=-=' * 10)
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint (0, 2)

print(''' Menu de Opções: 
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')
jogador = int(input('Qual a sua escolha: '))
print('------------------------')

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

print('------------------------')

print(f'Coputador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('------------------------')

if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador VENCE')
    elif jogador == 2:
        print('Computador VENCE')
    else:
        print('Jogada inválida')

elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('Coputador VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador VENCE')
    else:
        print('Jogada inválida')

elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('Jogador VENCE')
    elif jogador == 1:
        print('Computador VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida')