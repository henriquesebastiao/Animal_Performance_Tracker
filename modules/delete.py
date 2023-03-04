# coding: utf-8

import os
import sqlite3


def clear():
    """Limpa a tela"""
    os.system('cls' if os.name == 'nt' else 'clear')


def delete():
    """Deleta um animal do banco de dados"""

    # Obtém a tabela do animal
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
        if identifier.isnumeric():
            break

        print('Consulta inválida!')
        print('Digite apenas números!\n')
    # Conexão com o banco de dados
    with sqlite3.connect('data/data_base.db') as connection:
        cursor = connection.cursor()

        # Deleta o animal
        cursor.execute(f'DELETE FROM {genus} WHERE id = {identifier}')
        connection.commit()

    print('Animal deletado com sucesso!')
