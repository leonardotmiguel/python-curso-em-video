# Desafio 026
# Faça um programa que leia uma frase pelo teclado e mostre:
# quantas vezes aparece a letra "A"
# em que posição ela aparece a primeira vez
# em que posição ela aparece a última vez

frase = str(input('Digite uma frase: '))
print(f'A letra A aparece {frase.count('A')} vezes na frase')