import sqlite3, os, sys
from modules import cadastro
from contextlib import closing

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

print('''Animal Control - v0.1\n
1 - Cadastrar animal
2 - Alterar animal
3 - Excluir animal
Ctrl+C - Sair\n''')

try:
    opcao = input('>>> ')

    if opcao == '1':
        registro = cadastro.cadastrar()
        with sqlite3.connect('data/animais.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                cursor.execute(f'''
                                    INSERT INTO animais (id, entrada, genero, sexo, categoria, raca, origem)
                                    VALUES ({registro[0]}, "{registro[1]}", "{registro[2]}", "{registro[3]}", "{registro[4]}", "{registro[5]}", "{registro[6]}")
                               ''')
                conexao.commit()
        print('\nAnimal cadastrado com sucesso!')
        input('Pressione ENTER voltar ao menu principal...')

    elif opcao == '2':
        pass
    
    elif opcao == '3':
        pass
    
except KeyboardInterrupt:
    print('\nSaindo...')
    sys.exit()