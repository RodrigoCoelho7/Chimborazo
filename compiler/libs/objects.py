

class DECLARATION:
    def __init__(self,ID):
        self.ID = ID
    
    def set_tipo(self,TIPO):
        self.tipo = TIPO

class PROGRAM:
    def __init__(self):
        self.declarations = {}
        self.statements = {}
    
    def add_variable(self,VAR):
        if VAR.ID in list(self.declarations.keys()):
            self.error('La Variable ya existe')
        self.declarations[VAR.ID] = VAR

    def add_function(self,FUNC):
        if FUNC.ID in list(self.declarations.keys()):
            self.error('La funcion ya existe')
        self.declarations[FUNC.ID] = FUNC
    
    def error(self,message):
        print('Semantic Error: '+message)


class FUNCTION(PROGRAM):
    def __init__(self,ID,TIPO,PARAMS):
        self.ID = ID
        self.TIPO = TIPO
        for param in PARAMS:
            self.add_variable(*param)
