class Bovino:
    def __init__(self, id, sexo, raca='nelore', peso=0.0, nascimento=None, tipo='bovino'):
        self.__id = id
        self.raca = raca
        self.sexo = sexo
        self.peso = peso
        self.nascimento = nascimento
        self.tipo = tipo
    
    def set_peso(self, peso):
        self.peso = peso
    
    def set_nascimento(self, nascimento):
        self.nascimento = nascimento
    
    def set_id(self, id):
        self.__id = id