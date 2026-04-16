# Desafio 022
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todas as letras minúsculas
# - Quantas letras ao todo (sem considerar espaços)
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome completo em maiúsculas é {nome.upper()}')
print(f'Seu nome completo em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome)- nome.count(' ')}')
print(f'Seu primeiro nome tem {nome.find(' ')}')