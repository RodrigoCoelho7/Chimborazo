

class DECLARATION:
    def __init__(self,ID,TIPO):
        self.tipo = TIPO
        self.ID = ID

class PROGRAM:
    def __init__(self):
        self.declarations = {}
        self.statements = {}
    
    def add_variable(self,ID,TIPO):
        if ID in list(self.declarations.keys()):
            self.error('La Variable ya existe')
        self.declarations[ID] = DECLARATION(ID,TIPO)

    def add_function(self,ID,PARAMS,TIPO):
        if ID in list(self.declarations.keys()):
            self.error('La funcion ya existe')
        self.declarations[ID] = FUNCTION(ID,PARAMS,TIPO)
    
    def error(self,message):
        print('Semantic Error: '+message)


class FUNCTION(PROGRAM):
    def __init__(self,ID,TIPO,PARAMS):
        self.ID = ID
        self.TIPO = TIPO
        for param in PARAMS:
            self.add_variable(*param)
