# Desafio 057
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

masc = 'm'
fem = 'f'

while masc != 'M':
    sexo = str(input('Digite seu sexo, M para masculino e F para feminino: ')).upper()
    print('Sexo correto.')
    if sexo != 'M':
        print('Sexo errado, digite novamente!')