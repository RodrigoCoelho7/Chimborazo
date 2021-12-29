
class DECLARATION:
    def __init__(self,ID,TIPO=None,memory=-1):
        self.ID = ID
        self.TIPO = TIPO
        self.memory = memory
    
    def set_tipo(self,TIPO):
        self.TIPO = TIPO

class PROGRAM:
    def __init__(self):
        self.declarations = {}
        self.statements = {}
        self.GP = 0
    
    def add_variable(self,VAR):
        if VAR.ID in list(self.declarations.keys()):
            print(list(self.declarations.keys()))
            self.error(VAR.ID+' Ya fue definida')
        self.declarations[VAR.ID] = VAR
    
    def get_Variable_by_memory(self,P):
        for key in self.declarations.keys():
            if self.declarations[key].memory == P:
                return key
        return None
    
    def error(self,message):
        print('Semantic Error: '+message)
    
    def add_condition(self,code,ID):
        self.statements[ID] = code
    
    def statements_code(self):
        code = ''
        for key in self.statements.keys():
            code += f'\n{key}: NOP\n{self.statements[key]}'
        return code


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