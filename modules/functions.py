import os

def clear():
    """
    Limpa a tela do terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')