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
        if not identifier.isnumeric():
            print('Consulta inválida!')
            print('Digite apenas números!\n')
        else:
            break

    # Conexão com o banco de dados
    with sqlite3.connect('data/data_base.db') as connection:
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

        # Consulta
        cursor.execute(f'SELECT * FROM {genus} WHERE id = {identifier}')
        result = cursor.fetchone()

        if result is None:
            print('Animal não encontrado!')
            print('Tente novamente!\n')

        # Imprime os resultados caso o animal seja bovino
        if len(result) == 7:
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
            print('Peso: ', result[6])

        # Imprime os resultados caso o animal não seja bovino
        else:
            print('Animal encontrado!\n')
            print('ID: ', result[0])
            print('Entrada: ', result[1])

            if result[2] == 'm':
                print('Sexo: Masculino')
            else:
                print('Sexo: Feminino')

            print('Raça: ', result[3])
            print('Origem: ', result[4])
            print('Peso: ', result[5])
