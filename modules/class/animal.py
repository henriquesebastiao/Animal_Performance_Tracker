class Animal:
    def __init__(self, identifier, entry_date, gender, race, origin, peso):
        self.__identifier = identifier
        self.__entry_date = entry_date
        self.__gender = gender
        self.__race = race
        self.__origin = origin
        self.__peso = peso
    
    def get_characteristics(self):
        """Retorna as características do animal.

        Returns:
            identifier (str): ID do animal.
            entry_date (str): Data de entrada do animal.
            gender (str): Gênero do animal.
            race (str): Raça do animal.
            origin (str): Origem do animal.
            peso (float): Peso do animal.
        """
        return self.__identifier, self.__entry_date, self.__gender, self.__race, self.__origin, self.__peso
    
    def set_identifier(self, identifier):
        """Altera o ID do animal.

        Args:
            identifier (int): ID do animal.
        """
        self.__identifier = identifier
    
    def set_peso(self, peso):
        """Altera o peso do animal.

        Args:
            peso (float): Peso do animal.
        """
        self.__peso = peso