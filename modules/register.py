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
        identifier = input('ID: ').strip()
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
        print('3 - Caprino')
        print('4 - Equino')
        genus = input('>>> ')
        if genus not in ['1', '2', '3', '4']:
            print('Gênero inválido!')
            print('Digite apenas 1, 2, 3 ou 4!\n')
        else:
            # Cadastro de bovinos
            if genus == '1':
                genus = 'bovinos'
                # Sexo
                clear()
                while True:
                    gender = input('Sexo: ').lower().strip()
                    if gender not in 'mf':
                        print('Sexo inválido!')
                        print('Digite apenas M ou F!\n')
                    else:
                        if gender == 'm':
                            gender = 'Macho'
                        else:
                            gender = 'Fêmea'
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
                                category = 'Bezerro'
                            elif category == '2':
                                category = 'Garrote'
                            elif category == '3':
                                category = 'Boi'
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
                                category = 'Bezerra'
                            elif category == '2':
                                category = 'Novilha'
                            elif category == '3':
                                category = 'Vaca'
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
                            race = 'Nelore'
                        elif race == '2':
                            race = 'Girolando'
                        elif race == '3':
                            race = 'Guzerá'
                        elif race == '4':
                            race = 'Senepol'
                        elif race == '5':
                            race = 'Gir Leiteiro'
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
                        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {genus} (
                            id INTEGER PRIMARY KEY,
                            entrada TEXT,
                            sexo TEXT,
                            categoria TEXT,
                            raca TEXT,
                            origem TEXT,
                            peso REAL
                        )''')

                        # Insere os dados no banco de dados
                        cursor.execute(f'''INSERT INTO {genus} (
                            id, entrada, sexo, categoria, raca, origem, peso
                        ) VALUES (?, ?, ?, ?, ?, ?, ?)''', (
                            identifier, entry_date, gender, category, race, origin, peso
                        ))
                        connection.commit()

                        print('\nAnimal cadastrado com sucesso!')
                        input('Pressione ENTER para continuar...')
                        break
            elif genus == '2':
                genus = 'suinos'
                # Sexo
                clear()
                while True:
                    gender = input('Sexo: ').lower().strip()
                    if gender not in 'mf':
                        print('Sexo inválido!')
                        print('Digite apenas M ou F!\n')
                    else:
                        if gender == 'm':
                            gender = 'Macho'
                        else:
                            gender = 'Fêmea'
                        break

                # Raça
                clear()
                while True:
                    print('\nRaça: ')
                    print('1 - Landrace')
                    print('2 - Duroc')
                    print('3 - Hampshire')
                    print('4 - Pietrain')
                    print('5 - Large White')
                    race = input('>>> ')
                    if race not in ['1', '2', '3', '4', '5']:
                        print('Raça inválida!')
                        print('Digite apenas 1, 2, 3, 4 ou 5!\n')
                    else:
                        if race == '1':
                            race = 'Landrace'
                        elif race == '2':
                            race = 'Duroc'
                        elif race == '3':
                            race = 'Hampshire'
                        elif race == '4':
                            race = 'Pietrain'
                        elif race == '5':
                            race = 'Large White'
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
                        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {genus} (
                            id INTEGER PRIMARY KEY,
                            entrada TEXT,
                            sexo TEXT,
                            raca TEXT,
                            origem TEXT,
                            peso REAL
                        )''')

                        # Insere os dados no banco de dados
                        cursor.execute(f'''INSERT INTO {genus} (
                            id, entrada, sexo, categoria, raca, origem, peso
                        ) VALUES (?, ?, ?, ?, ?, ?)''', (
                            identifier, entry_date, gender, race, origin, peso
                        ))
                        connection.commit()

                        print('\nAnimal cadastrado com sucesso!')
                        input('Pressione ENTER para continuar...')
                        break
            elif genus == '3':
                genus = 'caprinos'
                # Sexo
                clear()
                while True:
                    gender = input('Sexo: ').lower().strip()
                    if gender not in 'mf':
                        print('Sexo inválido!')
                        print('Digite apenas M ou F!\n')
                    else:
                        if gender == 'm':
                            gender = 'Macho'
                        else:
                            gender = 'Fêmea'
                        break

                # Raça
                clear()
                while True:
                    print('\nRaça: ')
                    print('1 - Boer')
                    print('2 - Saanen')
                    print('3 - Anglo Nubiana')
                    print('4 - Pardo Suíço')
                    print('5 - Moxotó')
                    race = input('>>> ')
                    if race not in ['1', '2', '3', '4', '5']:
                        print('Raça inválida!')
                        print('Digite apenas 1, 2, 3, 4 ou 5!\n')
                    else:
                        if race == '1':
                            race = 'Boer'
                        elif race == '2':
                            race = 'Saanen'
                        elif race == '3':
                            race = 'Anglo Nubiana'
                        elif race == '4':
                            race = 'Pardo Suíço'
                        elif race == '5':
                            race = 'Moxotó'
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
                        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {genus} (
                            id INTEGER PRIMARY KEY,
                            entrada TEXT,
                            sexo TEXT,
                            raca TEXT,
                            origem TEXT,
                            peso REAL
                        )''')

                        # Insere os dados no banco de dados
                        cursor.execute(f'''INSERT INTO {genus} (
                            id, entrada, sexo, categoria, raca, origem, peso
                        ) VALUES (?, ?, ?, ?, ?, ?)''', (
                            identifier, entry_date, gender, race, origin, peso
                        ))
                        connection.commit()

                        print('\nAnimal cadastrado com sucesso!')
                        input('Pressione ENTER para continuar...')
                        break
            elif genus == '4':
                genus = 'equinos'
                # Sexo
                clear()
                while True:
                    gender = input('Sexo: ').lower().strip()
                    if gender not in 'mf':
                        print('Sexo inválido!')
                        print('Digite apenas M ou F!\n')
                    else:
                        if gender == 'm':
                            gender = 'Macho'
                        else:
                            gender = 'Fêmea'
                        break

                # Raça
                clear()
                while True:
                    print('\nRaça: ')
                    print('1 - Mangalarga Marchador')
                    print('2 - Quarto de Milha')
                    print('3 - Crioulo')
                    print('4 - Pampa')
                    print('5 - Puro Sangue Inglês')
                    race = input('>>> ')
                    if race not in ['1', '2', '3', '4', '5']:
                        print('Raça inválida!')
                        print('Digite apenas 1, 2, 3, 4 ou 5!\n')
                    else:
                        if race == '1':
                            race = 'Mangalarga Marchador'
                        elif race == '2':
                            race = 'Quarto de Milha'
                        elif race == '3':
                            race = 'Crioulo'
                        elif race == '4':
                            race = 'Pampa'
                        elif race == '5':
                            race = 'Puro Sangue Inglês'
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
                        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {genus} (
                            id INTEGER PRIMARY KEY,
                            entrada TEXT,
                            sexo TEXT,
                            raca TEXT,
                            origem TEXT,
                            peso REAL
                        )''')

                        # Insere os dados no banco de dados
                        cursor.execute(f'''INSERT INTO {genus} (
                            id, entrada, sexo, categoria, raca, origem, peso
                        ) VALUES (?, ?, ?, ?, ?, ?)''', (
                            identifier, entry_date, gender, race, origin, peso
                        ))
                        connection.commit()

                        print('\nAnimal cadastrado com sucesso!')
                        input('Pressione ENTER para continuar...')
                        break
