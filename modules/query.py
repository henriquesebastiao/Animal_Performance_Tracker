# coding: utf-8

import sqlite3
import os


def clear():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def query():
    """Consulta um animal no banco de dados"""
    clear()
    while True:
        identifier = input('ID: ').strip()
        if identifier.isnumeric():
            break

        print('Consulta inválida!')
        print('Digite apenas números!\n')
    # Conexão com o banco de dados
    with sqlite3.connect('data/data_base.db') as connection:
        _extracted_from_query_13(connection, identifier)


# TODO Rename this here and in `query`
def _extracted_from_query_13(connection, identifier):
    cursor = connection.cursor()

    # Obtém a tabela do animal
    while True:
        clear()
        print('Informe o gênero do animal:')
        print('1 - Bovino')
        print('2 - Suíno')
        print('3 - Caprino')
        print('4 - Equino')
        genus = input('>>> ').strip()
        
        if genus not in ('1', '2', '3', '4'):
            print('Opção inválida!')
            print('Tente novamente!\n')
        else:
            match genus:
                case '1':
                    genus = 'bovinos'
                    break
                case '2':
                    genus = 'suinos'
                    break
                case '3':
                    genus = 'caprinos'
                    break
                case '4':
                    genus = 'equinos'
                    break

    # Consulta
    cursor.execute(f'SELECT * FROM {genus} WHERE id = {identifier}')
    result = cursor.fetchone()

    if result is None:
        print('Animal não encontrado!')
        print('Tente novamente!\n')

        # Imprime os resultados caso o animal seja bovino
    if len(result) == 7:
        _extracted_from_query_50(result, 'Categoria: ', 'Raça: ', 'Origem: ')
        print('Peso: ', result[6])

    else:
        _extracted_from_query_50(result, 'Raça: ', 'Origem: ', 'Peso: ')


# TODO Rename this here and in `query`
def _extracted_from_query_50(result, arg1, arg2, arg3):
    print('Animal encontrado!\n')
    print('ID: ', result[0])
    print('Entrada: ', result[1])

    if result[2] == 'm':
        print('Sexo: Masculino')
    else:
        print('Sexo: Feminino')

    print(arg1, result[3])
    print(arg2, result[4])
    print(arg3, result[5])
