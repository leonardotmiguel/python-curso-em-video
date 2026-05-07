# Desafio 058
# Melhore o jogo do Desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
cont = 1
computador = randint(0, 10)
jogador = int(input('Digite um número para adivinhar: '))
print(f'Você digitou {jogador}')
print(f'Computador digitou {computador}')
if jogador != computador:
    print('Você errou...')
    while