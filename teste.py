n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
m = (n1 + n2) / 2
print(f'Sua media é {m:.1f}')
if m >= 6:
    print('Sua nota é boa')
else:
    print('Sua media foi ruim')