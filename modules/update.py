import os
import sqlite3
from contextlib import closing


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def update():
    while True:
        clear()
        print('Informe o gênero do animal:')
        print('1 - Bovino')
        print('2 - Suíno')
        print('3 - Caprino')
        print('4 - Equino')
        genus = input('>>> ').strip()
        if genus == '1':
            genus = 'bovinos'
            break
        elif genus == '2':
            genus = 'suinos'
            break
        elif genus == '3':
            genus = 'caprinos'
            break
        elif genus == '4':
            genus = 'equinos'
            break
        else:
            print('Opção inválida!')
            print('Tente novamente!\n')

    while True:
        clear()
        identifier = input('ID do animal: ').strip()
        if not identifier.isnumeric():
            print('Consulta inválida!')
            print('Digite apenas números!\n')
        else:
            break

    while True:
        clear()
        print('Informe a característica que deseja alterar:')
        print('1 - ID')
        print('2 - Data de entrada')
        print('3 - Peso')
        caracteristica = input('>>> ').strip()

        if caracteristica not in '123':
            print('Opção inválida!')
            print('Tente novamente!\n')
        else:
            break

    if caracteristica == '1':
        caracteristica = 'id'
    elif caracteristica == '2':
        caracteristica = 'entrada'
    elif caracteristica == '3':
        caracteristica = 'peso'

    while True:
        clear()
        valor = input('Novo valor: ').strip()
        if not valor.isnumeric():
            print('Consulta inválida!')
            print('Digite apenas números!\n')
        else:
            break

    with closing(sqlite3.connect('data/data_base.db')) as connection:
        cursor = connection.cursor()
        cursor.execute(f'UPDATE {genus} SET {caracteristica} = {valor} WHERE id = {identifier}')
        connection.commit()
        print('Animal atualizado com sucesso!')
