import datetime
import os
import sqlite3
from contextlib import closing


def clear():
    """Esta função limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def cadastrar():
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
        id_tag = input('ID: ').lower().strip()
        if not id_tag.isnumeric():
            print('ID inválido!')
            print('Digite apenas números!\n')
        else:
            break

    # Entrada
    clear()
    entrada = input('Data de entrada: ')

    if entrada == '':
        entrada = datetime.datetime.now().strftime('%d/%m/%Y')

    # Gênero
    clear()
    while True:
        print('\nGênero: ')
        print('1 - Bovino')
        print('2 - Suíno')
        print('4 - Caprino')
        print('5 - Equino')
        genero = input('>>> ')
        if genero not in ['1', '2', '4', '5']:
            print('Gênero inválido!')
            print('Digite apenas 1, 2, 4 ou 5!\n')
        else:
            # Cadastro de bovinos
            if genero == '1':
                genero = 'bovinos'

                # Sexo
                clear()
                while True:
                    sexo = input('Sexo: ').lower().strip()
                    if sexo not in 'mf':
                        print('Sexo inválido!')
                        print('Digite apenas M ou F!\n')
                    else:
                        break

                # Categoria
                clear()
                if sexo == 'm':
                    while True:
                        print('\nCategoria: ')
                        print('1 - Bezerro')
                        print('2 - Garrote')
                        print('3 - Boi')
                        categoria = input('>>> ')

                        if categoria not in ['1', '2', '3']:
                            print('Categoria inválida!')
                            print('Digite apenas 1, 2 ou 3!\n')
                        else:
                            if categoria == '1':
                                categoria = 'bezerro'
                            elif categoria == '2':
                                categoria = 'garrote'
                            elif categoria == '3':
                                categoria = 'boi'
                            break
                else:
                    while True:
                        print('\nCategoria: ')
                        print('1 - Bezerra')
                        print('2 - Novilha')
                        print('3 - Vaca')
                        categoria = input('>>> ')

                        if categoria not in ['1', '2', '3']:
                            print('Categoria inválida!')
                            print('Digite apenas 1, 2 ou 3!\n')
                        else:
                            if categoria == '1':
                                categoria = 'bezerra'
                            elif categoria == '2':
                                categoria = 'novilha'
                            elif categoria == '3':
                                categoria = 'vaca'
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
                    raca = input('>>> ')
                    if raca not in ['1', '2', '3', '4', '5']:
                        print('Raça inválida!')
                        print('Digite apenas 1, 2, 3, 4 ou 5!\n')
                    else:
                        if raca == '1':
                            raca = 'nelore'
                        elif raca == '2':
                            raca = 'girolando'
                        elif raca == '3':
                            raca = 'guzerá'
                        elif raca == '4':
                            raca = 'senepol'
                        elif raca == '5':
                            raca = 'gir leiteiro'
                        break

                # Origem
                clear()
                origem = input('\nOrigem: ')

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

                with sqlite3.connect('data/data_base.db') as conexao:
                    with closing(conexao.cursor()) as cursor:

                        # Cria a tabela animais caso ela não exista
                        cursor.execute(
                            'CREATE TABLE IF NOT EXISTS bovinos ('
                            'id INTEGER PRIMARY KEY,'
                            'entrada TEXT, -- Data e hora de entrada do animal (dd/mm/aaaa)'
                            'genero TEXT, -- Gênero do animal (bovinos, suínos, caprinos, equinos)'
                            'sexo TEXT, -- Sexo do animal (m - macho, f - fêmea)'
                            'categoria TEXT, -- Categoria do animal (bezerro, garrote, boi, bezerra, novilha, vaca)'
                            'raca TEXT, -- Raça do animal (nelore, girolando, guzerá, senepol, gir leiteiro)'
                            'origem TEXT, -- Origem do animal (Onde foi comprado))'
                            'peso FLOAT -- Peso do animal (em quilos)'
                            ')'
                        )

                        # Insere os dados no banco de dados
                        cursor.execute(
                            'INSERT INTO bovinos ('
                            'id,'
                            'entrada,'
                            'genero,'
                            'sexo,'
                            'categoria,'
                            'raca,'
                            'origem,'
                            'peso',
                            ') VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                            (id_tag, entrada, genero, sexo, categoria, raca, origem, peso),
                        )
                        conexao.commit()

                        print('\nAnimal cadastrado com sucesso!')
                        input('Pressione ENTER para continuar...')
                        break
            elif genero == '2':
                # genero = 'suínos'
                pass
            elif genero == '4':
                # genero = 'caprinos'
                pass
            elif genero == '5':
                # genero = 'equinos'
                pass
