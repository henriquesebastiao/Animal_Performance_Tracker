import os
import sys

from modules import cadastro


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
        cadastro.cadastrar()
    elif opcao == '2':
        pass

    elif opcao == '3':
        pass

except KeyboardInterrupt:
    print('\nSaindo...')
    sys.exit()
