

class DECLARATION:
    def __init__(self,ID,TIPO=None):
        self.ID = ID
        self.TIPO = TIPO
    
    def set_tipo(self,TIPO):
        self.TIPO = TIPO

class PROGRAM:
    def __init__(self):
        self.declarations = {}
        self.statements = {}
    
    def add_variable(self,VAR):
        if VAR.ID in list(self.declarations.keys()):
            self.error(VAR.ID+' Ya fue definida')
        self.declarations[VAR.ID] = VAR
    
    def error(self,message):
        print('Semantic Error: '+message)


class FUNCTION(PROGRAM):
    def __init__(self,ID,TIPO,PARAMS,RETURN):
        super().__init__()
        self.ID = ID
        self.TIPO = TIPO
        if RETURN[0] != 'ID':
            if RETURN[0] != TIPO:
                print(f'El tipo {RETURN[0].upper()} devuleto por la funcion no corresponde al definido anteriormente {TIPO.upper()}')
                exit()
        self.RETURN = RETURN
        for param in PARAMS:
            self.add_variable(param)
    
    def valida_tipo(self):
        if self.RETURN[0] == 'ID':
            if self.RETURN[1] in list(self.declarations.keys()):
                if self.declarations[self.RETURN[1]].TIPO != self.TIPO:
                    print(f'El tipo {self.declarations[self.RETURN[1]].TIPO.upper()} devuleto por la funcion no corresponde al definido anteriormente {self.TIPO.upper()}')
                    exit()
            else:
                print(f'No existe el ID {self.RETURN[1]}',list(self.declarations.keys()))
                exit()