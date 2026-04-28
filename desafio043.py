# Desafio 043
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

print('=-=' * 10)
print('        CÁLCULO DE IMC')
print('=-=' * 10)

altura = float(input('Sua altura: '))
peso = float(input('Seu peso: '))
imc = peso / (altura ** 2)

print(f'Seu IMC é de {imc:.1f}')
if imc <= 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
