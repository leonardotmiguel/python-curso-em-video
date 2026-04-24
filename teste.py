nome = str(input('Qual é o seu nome? '))
if nome == 'Leonardo':
    print('Que nome bonito!')

elif nome == 'Pedro' or nome == 'João' or nome == 'Lucas':
    print('Seu nome é bem comum no Brasil')

elif nome in 'Ana Cláudia Jéssica':
    print('Belo nome')

else:
    print('Seu nome é bem normal.')


print(f'Tenha um bom dia, {nome}!')