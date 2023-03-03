import os
import sys

from modules import register, query, update, delete


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()

print('''Animal Control - v0.1\n
1 - Cadastrar animal
2 - Consultar animal
3 - Alterar animal
4 - Excluir animal
Ctrl+C - Sair\n''')

try:
    opcao = input('>>> ')

    if opcao == '1':
        register.register()
    elif opcao == '2':
        query.query()
    elif opcao == '3':
        update.update()
    elif opcao == '4':
        delete.delete()

except KeyboardInterrupt:
    print('\nSaindo...')
    sys.exit()
