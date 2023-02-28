import sqlite3
from contextlib import closing

with sqlite3.connect('data/animais.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('''
                            CREATE TABLE animais (id text, entrada text, genero text, sexo text, categoria text, raca text, origem text)
                       ''')
        conexao.commit()