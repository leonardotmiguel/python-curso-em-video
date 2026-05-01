# Desafio 048
# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0
for contagem in range(1, 501, 2):
    if contagem % 3 == 0:
        cont = cont + 1
        soma = soma + contagem
print(f'A soma entre todos os {cont} números ímpares é {soma}')