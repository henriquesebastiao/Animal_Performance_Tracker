import datetime
import os
import sqlite3
from contextlib import closing


def clear():
    """Esta função limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def register():
    """Esta função recebe os dados do animal e os insere no banco de dados.

    Returns:
        id (str): ID do animal.
        entrada (str): Data e hora de entrada do animal.
        sexo (str): Sexo do animal.
        categoria (str): Categoria do animal.
        raca (str): Raça do animal.
        origem (str): Origem do animal.
    """

    # ID
    clear()
    while True:
        identifier = input('ID: ').lower().strip()
        if not identifier.isnumeric():
            print('ID inválido!')
            print('Digite apenas números!\n')
        else:
            break

    # Entrada
    clear()
    entry_date = input('Data de entrada: ')

    if entry_date == '':
        entry_date = datetime.datetime.now().strftime('%d/%m/%Y')

    # Gênero
    clear()
    while True:
        print('\nGênero: ')
        print('1 - Bovino')
        print('2 - Suíno')
        print('4 - Caprino')
        print('5 - Equino')
        genus = input('>>> ')
        if genus not in ['1', '2', '4', '5']:
            print('Gênero inválido!')
            print('Digite apenas 1, 2, 4 ou 5!\n')
        else:
            # Cadastro de bovinos
            if genus == '1':
                # Sexo
                clear()
                while True:
                    gender = input('Sexo: ').lower().strip()
                    if gender not in 'mf':
                        print('Sexo inválido!')
                        print('Digite apenas M ou F!\n')
                    else:
                        break

                # Categoria
                clear()
                if gender == 'm':
                    while True:
                        print('\nCategoria: ')
                        print('1 - Bezerro')
                        print('2 - Garrote')
                        print('3 - Boi')
                        category = input('>>> ')

                        if category not in ['1', '2', '3']:
                            print('Categoria inválida!')
                            print('Digite apenas 1, 2 ou 3!\n')
                        else:
                            if category == '1':
                                category = 'bezerro'
                            elif category == '2':
                                category = 'garrote'
                            elif category == '3':
                                category = 'boi'
                            break
                else:
                    while True:
                        print('\nCategoria: ')
                        print('1 - Bezerra')
                        print('2 - Novilha')
                        print('3 - Vaca')
                        category = input('>>> ')

                        if category not in ['1', '2', '3']:
                            print('Categoria inválida!')
                            print('Digite apenas 1, 2 ou 3!\n')
                        else:
                            if category == '1':
                                category = 'bezerra'
                            elif category == '2':
                                category = 'novilha'
                            elif category == '3':
                                category = 'vaca'
                            break

                # Raça
                clear()
                while True:
                    print('\nRaça: ')
                    print('1 - Nelore')
                    print('2 - Girolando')
                    print('3 - Guzerá')
                    print('4 - Senepol')
                    print('5 - Gir Leiteiro')
                    race = input('>>> ')
                    if race not in ['1', '2', '3', '4', '5']:
                        print('Raça inválida!')
                        print('Digite apenas 1, 2, 3, 4 ou 5!\n')
                    else:
                        if race == '1':
                            race = 'nelore'
                        elif race == '2':
                            race = 'girolando'
                        elif race == '3':
                            race = 'guzerá'
                        elif race == '4':
                            race = 'senepol'
                        elif race == '5':
                            race = 'gir leiteiro'
                        break

                # Origem
                clear()
                origin = input('\nOrigem: ')

                # Peso
                clear()
                while True:
                    peso = input('\nPeso: ')
                    try:
                        peso = float(peso)
                        break
                    except ValueError:
                        print('Peso inválido!')
                        print('Digite apenas números!\n')

                with sqlite3.connect('data/data_base.db') as connection:
                    with closing(connection.cursor()) as cursor:

                        # Cria a tabela animais caso ela não exista
                        cursor.execute('''CREATE TABLE IF NOT EXISTS bovinos (
                            id INTEGER PRIMARY KEY,
                            entrada TEXT,
                            sexo TEXT,
                            categoria TEXT,
                            raca TEXT,
                            origem TEXT,
                            peso REAL
                        )''')

                        # Insere os dados no banco de dados
                        cursor.execute('''INSERT INTO bovinos (
                            id, entrada, sexo, categoria, raca, origem, peso
                        ) VALUES (?, ?, ?, ?, ?, ?, ?)''', (
                            identifier, entry_date, gender, category, race, origin, peso
                        ))
                        connection.commit()

                        print('\nAnimal cadastrado com sucesso!')
                        input('Pressione ENTER para continuar...')
                        break
            elif genus == '2':
                # genus = 'suínos'
                pass
            elif genus == '4':
                # genus = 'caprinos'
                pass
            elif genus == '5':
                # genus = 'equinos'
                pass
