# Desafio 029
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.

velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print(f'Você foi multado! Seu limite de velocidade excedeu os 80km/h, você deverá pagar uma multa no valor de R$ {(velocidade - 80) * 7}')
else:
    print('Você está dentro do limite de velocidade')
print('Tenha uma boa viagem!')