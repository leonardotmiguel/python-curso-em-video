# Desafio 037
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

num = int(input('Digite um número inteiro: '))
print('''Escolhe uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Conerter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual à {bin(num)}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual à {oct(num)}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual à {hex(num)}')
else:
    print('Opção inválida, tente novamente.')