# Desafio 039
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano de seu nascimento: '))
ano = atual - nascimento
print(f'Quem nasceu em {nascimento} tem {ano} anos em {atual}')
if ano == 18:
    print('É hora de se alistar!')
elif ano < 18:
    saldo = 18 - ano
    print(f'Ainda falta {saldo} ano(s) para você se alistar!')
    alistamento = atual + saldo
    print(f'Seu alistamento será no ano de {alistamento}')
elif ano > 18:
    saldo = ano - 18
    print(f'Você deveria ter se alistado há {saldo} anos')
    alistamento = atual - saldo
    print(f'Seu alistamento seria no ano de {alistamento}')