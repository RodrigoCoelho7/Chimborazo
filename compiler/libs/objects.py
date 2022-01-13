
class DECLARATION:
    def __init__(self,ID,TOKEN=None,TIPO=None,memory=-1):
        self.ID = ID
        self.TOKEN = TOKEN
        self.TIPO = TIPO
        self.memory = memory
    
    def set_tipo(self,TIPO):
        if self.TOKEN is None or self.TOKEN == TIPO:
            self.TIPO = TIPO
            return (True,TIPO)
        else:
            if self.TOKEN == 'entero' and TIPO == 'real':
                self.TIPO = TIPO
                print(f'Warning: El tipo fue corregido automaticamente {self.ID}: {self.TOKEN}, {TIPO}')
                return (True,TIPO)
            print(f'Semantic Error: Verifique el tipo de la atribucion, {self.ID}: recibio {self.TOKEN}, esperaba {TIPO}')
            return (False,None)

class PROGRAM:
    def __init__(self):
        self.declarations = {}
        self.statements = {}
        self.memory = ''
        self.GP = 0
        self.success = True
    
    def get_push(self,decl):
        return f'\tPUSHG {self.declarations[decl].memory}\n'
    
    def get_store(self,decl=None):
        if decl is None:
            return f'\tSTOREG {self.GP}\n'
        else:
            return f'\tSTOREG {self.declarations[decl].memory}\n'
    
    def count_pointer(self):
        self.GP += 1

    def add_memory(self,memory):
        self.memory = self.memory + memory

    def add_variable(self,VAR):
        if VAR.ID in list(self.declarations.keys()):
            self.error(f'La variable {VAR.ID} ya fue definida')
        self.declarations[VAR.ID] = VAR
    
    def error(self,message):
        print('Semantic Error: '+message)
        self.success = False
    
    def add_condition(self,code,ID):
        self.statements[ID] = code
    
    def add_function(self,code,ID):
        self.statements[ID] = code

    def statements_code(self):
        code = ''
        for key in self.statements.keys():
            code += f'\n{key}: NOP\n{self.statements[key]}'
        return code


class FUNCTION(PROGRAM):
    def __init__(self):
        super().__init__()
        self.params = {}
        self.num_param = 0
        self.count_pointer()
        get_store = property(doc='(!) Disallowed inherited')
        count_pointer = property(doc='(!) Disallowed inherited')
        get_push = property(doc='(!) Disallowed inherited')
    
    def clean(self):
        return f'\tPOP {abs(self.GP+1)}\n'
    
    def add_memory(self,memory):
        self.memory = memory + self.memory

    def get_push(self,decl):
        return f'\tPUSHL {self.declarations[decl].memory}\n'

    def get_store(self,decl=None):
        if decl is None:
            return f'\tSTOREL {self.GP}\n'
        else:
            return f'\tSTOREL {self.declarations[decl].memory}\n'

    def count_pointer(self):
        self.GP -= 1
    
    
    def set_ID(self,ID):
        self.ID = ID
    
    def set_Return(self,RETURN):
        if RETURN[0] != 'ID':
            if RETURN[0] != self.TIPO:
                self.error(f'El tipo {RETURN[0].upper()} devuleto por la funcion {self.ID} no corresponde al definido anteriormente {self.TIPO.upper()}')
                
        self.RETURN = RETURN
    
    def set_paramns(self,PARAMS):
        for param in PARAMS:
            self.add_variable(param)
            self.params[param.ID] = param.TIPO
        self.num_param = len(list(self.params.keys()))

    def set_tipo(self,TIPO):
        self.TIPO = TIPO

    def valida_tipo(self):
        if self.RETURN[0] == 'ID':
            if self.RETURN[1] in list(self.declarations.keys()):
                if self.declarations[self.RETURN[1]].TIPO != self.TIPO:
                    self.error(f'El tipo {self.declarations[self.RETURN[1]].TIPO.upper()} devuleto por la funcion no corresponde al definido anteriormente {self.TIPO.upper()}')
                    
            else:
                self.error(f'No existe el ID {self.RETURN[1]}')
                