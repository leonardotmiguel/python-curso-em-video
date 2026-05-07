num = 1
cont = 0
while num != 0:
    num = int(input('Digite um número: '))
    if num != 0:
        cont += 1

print(f'Você digitou {cont} vezes antes de digitar o zero.')
