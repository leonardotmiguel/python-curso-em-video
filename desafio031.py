# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km e R$ 0,45 para viagens mais longas.

distancia = float(input('Digite a distância da viagem: '))

if distancia <= 200:
    print(f'Sua viagem custará R$ {distancia * 0.50:.2f}')
else:
    print(f'Sua viagem custará R$ {distancia * 0.45:.2f}')