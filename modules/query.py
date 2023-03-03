import sqlite3
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def query():
    clear()
    while True:
        identifier = input('ID: ').strip()
        if not identifier.isnumeric():
            print('Consulta inválida!')
            print('Digite apenas números!\n')
        else:
            break

    # Conexão com o banco de dados
    with sqlite3.connect('data/data_base.db') as connection:
        cursor = connection.cursor()

        # Consulta
        cursor.execute(f'SELECT * FROM bovinos WHERE id = {identifier}')
        result = cursor.fetchone()

        if result is None:
            print('Animal não encontrado!')
            print('Tente novamente!\n')
        else:
            print('Animal encontrado!\n')
            print('ID: ', result[0])
            print('Entrada: ', result[1])

            if result[2] == 'm':
                print('Sexo: Masculino')
            else:
                print('Sexo: Feminino')

            print('Categoria: ', result[3])
            print('Raça: ', result[4])
            print('Origem: ', result[5])
