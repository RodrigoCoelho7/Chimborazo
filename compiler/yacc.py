import ply.yacc as yacc
from Lex import tokens, find_column
import re
from libs.objects import PROGRAM, DECLARATION, FUNCTION
from libs.functions import allocate_memory,operator,ID_generator,write_f,cast,make_cast
import libs.file_writer as file_writer
import libs.code as code


def p_prg(p):
    "prg : declarations statements"
    p.parser.code = p.parser.program.memory + p.parser.code + p[1][0] + p[2] + '\tSTOP\n' + p.parser.program.statements_code()

#-------------- Declarations ------------------------------

def p_declarations_1(p):
    "declarations : decl"
    if len(p[1][1] ) > 0:
        for decl in p[1][1]:
            p.parser.program.add_variable(decl)
        tipo = decl.TIPO
        N = len(p[1][1])
        if not p.parser.flag_function:
            p.parser.program.add_memory(allocate_memory(N,tipo))
        else:
            p.parser.flag_function = False
        p.parser.declarations = []
        p[0] = [p[1][0],[]]
    else:
        p[0] = ['',[]]

def p_declarations_mult(p):
    "declarations : declarations decl"
    for decl in p[1][1]+p[2][1]:
        p.parser.program.add_variable(decl)
    tipo = decl.TIPO
    N = len(p[1][1]+p[2][1])
    if not p.parser.flag_function:
        p.parser.program.add_memory(allocate_memory(N,tipo))
    else:
        p.parser.flag_function = False
    p.parser.declarations = []            
    p[0] = [p[1][0] + p[2][0],[]]

def p_decl_V(p):
    "decl : declV"
    p[0] = p[1]

def p_decl_F(p):
    "decl : declF"
    p.parser.program.success = p[1][1][0].success and p.parser.program.success
    p[0] = p[1]

def p_decl_L(p):
    "decl : declL"

#---------------------------------------------------------------

#----------------- Variable declarations ----------------------------

def p_declV(p):
    "declV : VAR vari ':' tipo"
    is_correct = True
    tipo = None
    for var in p[2][1]:
        aux = var.set_tipo(p[4])
        is_correct = is_correct and aux[0]
        tipo = aux[1]
    if is_correct:
        if tipo == 'real':
            p[2][0] = re.sub(r'\tITOF\n',r'',p[2][0])
            p[2][0] = re.sub(r'PUSHI ([0-9]+)',r'PUSHF \1.0',p[2][0])
        p[0] = p[2]
    else:
        p[0] = p[2]
        p.parser.success = False

def p_vari_atrib(p):
    "vari : atribD"
    p[0] = p[1]

def p_vari_id(p):
    "vari : ID"
    p[0] = ['',[DECLARATION(p[1],memory=p.parser.program.GP)]]
    p.parser.program.count_pointer()

def p_vari_atribs(p):
    "vari : vari ',' atribD"
    p[0] = [p[1][0] + p[3][0],p[1][1] + p[3][1]]

def p_vari_ids(p):
    "vari : vari ',' ID"
    p[0] = [p[1][0]+'',p[1][1]+[DECLARATION(p[3],memory=p.parser.program.GP)]]
    p.parser.program.count_pointer()

def p_tipo_int(p):
    "tipo : ENTERO"
    p[0]= p[1]

def p_tipo_REAL(p):
    "tipo : REAL"
    p[0] = p[1]
    p.parser.cast = False

def p_tipo_BOOL(p):
    "tipo : BOOLEANO"
    p[0] = p[1]

def p_tipo_STRING(p):
    "tipo : STR"
    p[0] = p[1]

def p_atribD_string(p):
    "atribD : ID '=' STRING"
    p[0] = [f'\tPUSHS {p[3]}\n{p.parser.program.get_store()}',[DECLARATION(p[1],TOKEN='string',memory=p.parser.program.GP)]]
    p.parser.program.count_pointer()

def p_atribD_true(p):
    "atribD : ID '=' VERDADERO"
    p[0] = [f'\tPUSHI 1\n{p.parser.program.get_store()}',[DECLARATION(p[1],TOKEN='booleano',memory=p.parser.program.GP)]]
    p.parser.program.count_pointer()

def p_atribD_false(p):
    "atribD : ID '=' FALSO"
    p[0] = [f'\tPUSHI 0\n{p.parser.program.get_store()}',[DECLARATION(p[1],TOKEN='booleano',memory=p.parser.program.GP)]]
    p.parser.program.count_pointer()

def p_atribD(p):
    "atribD : ID '=' exp"
    p[0] = [p[3][0] + f'{p.parser.program.get_store()}',[DECLARATION(p[1],TOKEN=p[3][1],memory=p.parser.program.GP)]]
    p.parser.program.count_pointer()

#------------------------------------------------------

#-----------------List Declarations --------------------------

def p_declL(p):
    "declL : LISTA ID '=' lista"
    p.parser.declarations.append(DECLARATION(p[4],TIPO="lista"))
    p[0] = p[1] + ' ' + p[2] + p[3] + p[4]

def p_lista_vazia(p):
    "lista : '[' ']'"
    p[0] = p[1] + p[2]

def p_lista_elem(p):
    "lista : '[' elementos ']'"
    p[0] = p[1] + str(p[2]) + p[3]

def p_elementos_1(p):
    "elementos : elemento"
    p[0] = str(p[1])

def p_elementos_mult(p):
    "elementos : elementos ',' elemento"
    p[0] = str(p[1]) + p[2] + str(p[3])

def p_elemento_INT(p):
    "elemento : INT"
    p[0] = p[1]
    parser.comp_lista += 1

def p_elemento_FLOAT(p):
    "elemento : FLOAT"
    p[0] = p[1]
    parser.comp_lista += 1

def p_elemento_BOOL(p):
    "elemento : BOOLEANO"
    p[0] = p[1]
    parser.comp_lista += 1

def p_elemento_STRING(p):
    "elemento : STRING"
    p[0] = p[1]
    parser.comp_lista += 1

def p_elemento_ID(p):
    "elemento : ID"
    p[0] = p[1]
    parser.comp_lista += 1

def p_elemento_lista(p):
    "elemento : lista"
    p[0] = p[1]

#-------------------------------------------------------

#-------------------Function declarations ------------------

def p_declF_parametros(p):
    "declF : FUNCION ID '(' parametros ')' ':' tipo declarations statements DEVUELVE return '.'"
    f = p.parser.program
    p.parser.program = p.parser.save_program
    p.parser.save_program = None
    f.set_ID(p[2])
    f.set_tipo(p[7])
    f.set_Return(p[11][1])
    f.valida_tipo()
    p.parser.program.add_function(p[8][0]+p[9]+p[11][0]+f'\tSTOREL {f.GP}\n\tRETURN\n' + f.statements_code(),p[2])
    p.parser.flag_function = True
    p[0] = ['',[f]]
    
def p_parametros_0(p):
    "parametros : "
    if p.parser.save_program is None:
        p.parser.save_program = p.parser.program
        p.parser.program = FUNCTION()
        p[0] = ''
    else:
        print(f'Fatal Error: No es posible definir funciones dentro de funciones')
        exit()

def p_parametros_1(p):
    "parametros : ID ':' tipo"
    if p.parser.save_program is None:
        p.parser.save_program = p.parser.program
        p.parser.program = FUNCTION()
        p.parser.program.set_paramns([DECLARATION(p[1],TIPO=p[3],memory=p.parser.program.GP)])
        p.parser.program.count_pointer()
        p[0] = ''
    else:
        print(f'Fatal Error: No es posible definir funciones dentro de funciones')
        exit()

def p_parametros_mult(p):
    "parametros : parametros ',' ID ':' tipo"
    if p.parser.save_program is None:
        p.parser.save_program = p.parser.program
        p.parser.program = FUNCTION()
    p.parser.program.set_paramns([DECLARATION(p[3],TIPO=p[5],memory=p.parser.program.GP)])
    p.parser.program.count_pointer()
    p[0] = ''

def p_return_INT(p):
    "return : INT"
    p[0] = [f'\tPUSHI {p[1]}\n',('entero',p[1])]

def p_return_ID(p):
    "return : ID"
    if p[1] not in list(p.parser.program.declarations.keys()) and p[1] in list(p.parser.save_program.declarations.keys()) and type(p.parser.save_program.declarations[p[1]]) is FUNCTION:
        print(f'Semantic Error: No es posible usar funciones o su resultado como parametro de devuelve. Experimente usar una variable auxiliar. lin {p.lexer.lineno}')
        p.success = False
        p[0] =['',('ID','Sin Tipo')]
    else:
        if p[1] not in list(p.parser.program.declarations.keys()):
            print(f'Semantic Error:La variable {p[1]} no se encuentra definida. lin {p.lexer.lineno}')
            p.success = False
            p[0] =['',('ID','Sin Tipo')]
        else:
            p[0] = [f'\tPUSHL {p.parser.program.declarations[p[1]].memory}\n',('ID',p[1])]

def p_return_FLOAT(p):
    "return : FLOAT"
    p[0] = [f'\tPUSHF {p[1]}\n',('real',p[1])]

def p_return_TRUE(p):
    "return : VERDADERO"
    p[0] = [f'\tPUSHI 1\n',('booleano',p[1])]

def p_return_FALSE(p):
    "return : FALSO"
    p[0] = [f'\tPUSHI 0\n',('booleano',p[1])]

#----------------------------------------------------------------------------

#----------------------STATEMENTS-------------------------------------------

def p_statements_1(p):
    "statements : stat"
    p[0] = p[1]

def p_statements_mult(p):
    "statements : statements stat"
    p[0] = p[1] + p[2]

def p_stat_atrib(p):
    "stat : atrib ';'"
    p[0] = p[1]

def p_stat_conditions(p):
    "stat : conditions"
    p[0] = p[1]

def p_stat_ciclos(p):
    "stat : ciclos"
    p[0] = p[1]

def p_stat_write(p):
    "stat : write"
    p[0] = p[1]


#-----------------ATRIBUIÇÕES-------------------------

def p_atrib_string(p):
    "atrib : ID '=' STRING"
    if 'string' == p.parser.program.declarations[p[1]].TIPO:
        p[0] = f'\tPUSHS {p[3]}\n{p.parser.program.get_store(p[1])}'
    else:
        print(f'Semantic Error: El tipo recibido: string, no coincide con el tipo: {p.parser.program.declarations[p[1]].TIPO}, esperado para {p[1]}. lin {p.lexer.lineno}')
    
def p_atrib_true(p):
    "atrib : ID '=' VERDADERO"
    if 'booleano' == p.parser.program.declarations[p[1]].TIPO:
        p[0] = f'\tPUSHI 1\n{p.parser.program.get_store(p[1])}'
    else:
        print(f'Semantic Error: El tipo recibido: booleano, no coincide con el tipo: {p.parser.program.declarations[p[1]].TIPO}, esperado para {p[1]}. lin {p.lexer.lineno}')
        p[0] = ''
        p.parser.success = False

def p_atrib_false(p):
    "atrib : ID '=' FALSO"
    if 'booleano' == p.parser.program.declarations[p[1]].TIPO:
        p[0] = f'\tPUSHI 0\n{p.parser.program.get_store(p[1])}'
    else:
        print(f'Semantic Error: El tipo recibido: booleano, no coincide con el tipo: {p.parser.program.declarations[p[1]].TIPO}, esperado para {p[1]}. lin {p.lexer.lineno}')
        p[0] = ''
        p.parser.success = False

def p_atrib(p):
    "atrib : ID '=' exp"
    if p[1] in list(p.parser.program.declarations.keys()):
        if p[3][1] == p.parser.program.declarations[p[1]].TIPO:
            p[0] = f'{p[3][0]}{p.parser.program.get_store(p[1])}'
        elif p[3][1] == 'entero' and p.parser.program.declarations[p[1]].TIPO == 'real':
            print(f'Warning: El tipo de las expresiones: {p[3][1]} no coincide con el de la variable: {p.parser.program.declarations[p[1]].TIPO }, esperado para {p[1]}. lin {p.lexer.lineno}')
            p[0] = f'{p[3][0]}\tITOF\n{p.parser.program.get_store(p[1])}'
        else:
            print(f'Semantic Error: El tipo recibido: {p[3][1]}, no coincide con el tipo: {p.parser.program.declarations[p[1]].TIPO}, esperado para {p[1]}. lin {p.lexer.lineno}')
            p[0] = ''
            p.parser.success = False
    else:
        print(f'Semantic Error: La variable {p[1]} no fue definida')
        p.parser.success = False
        p[0] = ''

def p_exp_soma(p):
    "exp : exp '+' termo"
    code = cast(p[1],p[3])
    if code is not None:
        if code[1] == 'string':
            p[0] = [f'{code[0]}CONCAT\n',code[1]]
        else:
            p[0] = [f'{code[0]}ADD\n',code[1]]
    else:
        print(f'Semantic Error: La operacion no se encuentra definida para ese tipo de datos: {p[1][1]}, {p[3][1]}. lin {p.lexer.lineno}')
        p[0] = ['','Sin Tipo']
        p.parser.success = False

def p_exp_sub(p):
    "exp : exp '-' termo"
    code = cast(p[1],p[3])
    if code is not None and code[1] != 'string':
        p[0] = [f'{code[0]}SUB\n',code[1]]
    else:
        print(f'Semantic Error: La operacion no se encuentra definida para ese tipo de datos: {p[1][1]}, {p[3][1]}. lin {p.lexer.lineno}')
        p[0] = ['','Sin Tipo']
        p.parser.success = False

def p_exp_termo(p):
    "exp : termo"
    p[0] = p[1]

def p_termo_mul(p):
    "termo : termo '*' fator"
    code = cast(p[1],p[3])
    if code is not None and code[1] != 'string':
        p[0] = [f'{code[0]}MUL\n',code[1]]
    else:
        print(f'Semantic Error: La operacion no se encuentra definida para ese tipo de datos: {p[1][1]}, {p[3][1]}. lin {p.lexer.lineno}')
        p[0] = ['','Sin Tipo']
        p.parser.success = False
    

def p_termo_div(p):
    "termo : termo '/' fator"
    code = cast(p[1],p[3])
    if code is not None and code[1] != 'string':
        p[0] = [f'{code[0]}DIV\n',code[1]]
    else:
        print(f'Semantic Error: La operacion no se encuentra definida para ese tipo de datos: {p[1][1]}, {p[3][1]}. lin {p.lexer.lineno}')
        p[0] = ['','Sin Tipo']
        p.parser.success = False

def p_termo_resto(p):
    "termo : termo RESTO fator"
    code = cast(p[1],p[3])
    if code is not None and code[1] != 'string':
        p[0] = [f'{code[0]}MOD\n',code[1]]
    else:
        print(f'Semantic Error: La operacion no se encuentra definida para ese tipo de datos: {p[1][1]}, {p[3][1]}. lin {p.lexer.lineno}')
        p[0] = ['','Sin Tipo']
        p.parser.success = False

def p_termo_pot(p):
    "termo : termo '^' fator"
    if p[3][1] != 'entero' and p[3][1] != 'real':
        print(f'Semantic Error: Potencia solamente definida para exponente entero o real. lin {p.lexer.lineno}')
        p[0] = ['','Sin Tipo']
        p.parser.success = False
    elif p[1][1] != 'entero' and p[1][1] != 'real':
        print(f'Semantic Error: Potencia solamente definida para base entera o real. lin {p.lexer.lineno}')
        p[0] = ['','Sin Tipo']
        p.parser.success = False
    else:
        if p[3][1] != 'real':
            c = '' if p[1][1] == 'entero' else 'F'
            p.parser.program.add_function(code.pot(c),'SYSPOTENCIA')
            push = '\tPUSHI 1\n' if p[1][1] == 'entero' else '\tPUSHF 1.0\n'
            p[0] = [f'{push}{p[3][0]}{p[1][0]}\tPUSHA SYSPOTENCIA\n\tCALL\n\tNOP\n\tPOP 2\n',p[1][1]]
        else:
            p.parser.program.add_function(code.logaritmo,'SYSLN')
            p.parser.program.add_function(code.exponencial,'SYSEXP')
            p.parser.program.add_function(code.potreal,'SYSPOTREAL')
            p.parser.program.add_function(code.pot('F'),'SYSPOTENCIA')
            p.parser.program.add_function(code.fact,'SYSFACTORIAL')
            print(f'Warning: La potencia de exponente real es una aproximacion y solo se encuentra definida para base positiva > 0. lin {p.lexer.lineno}')
            C = '\tITOF\n' if p[1][1] == 'entero' else ''
            p[0] = [f'\tPUSHF 0.0\n{p[3][0]}{p[1][0]}{C}\tPUSHA SYSPOTREAL\n\tCALL\n\tNOP\n\tPOP 2\n','real']


def p_fator_factorial(p):
    "fator : exp '!' "
    if p[1][1] != 'entero':
        print(f'Semantic Error: Factorial solamente definida para numero entero. lin {p.lexer.lineno}')
        p[0] = ['','Sin Tipo']
        p.parser.success = False
    else: 
        p.parser.program.add_function(code.fact,'SYSFACTORIAL')
        p[0] = [f'\tPUSHI 1\n{p[1][0]}\tPUSHA SYSFACTORIAL\n\tCALL\n\tNOP\n\tPOP 1\n',p[1][1]]

def p_fator_exp(p):
    "fator : EXP '(' exp ')'"
    if p[3][1] != 'entero' and p[3][1] != 'real':
        print(f'Semantic Error: Exponencial solamente definida para numero entero o real, lin {p.lexer.lineno}. lin {p.lexer.lineno}')
        p[0] = ['','Sin Tipo']
        p.parser.success = False
    else:
        p.parser.program.add_function(code.exponencial,'SYSEXP')
        p.parser.program.add_function(code.pot('F'),'SYSPOTENCIA')
        p.parser.program.add_function(code.fact,'SYSFACTORIAL')
        C = '\tITOF\n' if p[3][1] == 'entero' else ''
        p[0] = [f'\tPUSHF 0.0\n\tPUSHN 1\n{p[3][0]}{C}\tPUSHA SYSEXP\n\tCALL\n\tNOP\n\tPOP 2\n','real']
    
def p_fator_ln(p):
    "fator : LN '(' exp ')'"
    if p[3][1] != 'entero' and p[3][1] != 'real':
        print(f'Semantic Error: Logaritmo solamente definida para numero entero o real positivo, lin {p.lexer.lineno}. lin {p.lexer.lineno}')
        p[0] = ['','Sin Tipo']
        p.parser.success = False
    else:
        p.parser.program.add_function(code.logaritmo,'SYSLN')
        p.parser.program.add_function(code.pot('F'),'SYSPOTENCIA')
        C = '\tITOF\n' if p[3][1] == 'entero' else ''
        p[0] = [f'\tPUSHF 0.0\n\tPUSHN 1\n{p[3][0]}{C}\tPUSHA SYSLN\n\tCALL\n\tNOP\n\tPOP 2\n','real']

def p_termo_fator(p):
    "termo : fator"
    p[0] = p[1]

def p_fator_INT(p):
    "fator : INT"
    p[0] = [f'\tPUSHI {p[1]}\n','entero']

def p_fator_VERDADERO(p):
    "fator : VERDADERO"
    p[0] = [f'\tPUSHI 1\n','booleano']

def p_fator_FALSO(p):
    "fator : FALSO"
    p[0] = [f'\tPUSHI 0\n','booleano']

def p_fator_FLOAT(p):
    "fator : FLOAT"
    p[0] = [f'\tPUSHF {p[1]}\n','real']

def p_fator_STRING(p):
    "fator : STRING"
    p[0] = [f'\tPUSHS {p[1]}\n','string']

def p_fator_ID(p):
    "fator : ID"
    if p[1] in list(p.parser.program.declarations.keys()):
        p[0] = [p.parser.program.get_push(p[1]),p.parser.program.declarations[p[1]].TIPO]
    else:
        print(f'Semantic Error: La variable {p[1]} no fue definida')
        p[0] = ['','Sin Tipo']
        p.parser.success = False

def p_fator_FUNC(p):
    "fator : ID '(' content_params ')' "
    aux = None
    if p[1] in list(p.parser.program.declarations.keys()):
        aux = p.parser.program.declarations[p[1]]
        pr = p.parser.program
    elif p.parser.save_program is not None:
        if p[1] in list(p.parser.save_program.declarations.keys()):
            aux = p.parser.save_program.declarations[p[1]]
            pr = p.parser.save_program
        else:
            print(f'Semantic Error: La funcion {p[1]} no fue definida')
            p[0] = ['','Sin Tipo']
            p.parser.success = False
    else:
            print(f'Semantic Error: La funcion {p[1]} no fue definida')
            p[0] = ['','Sin Tipo']
            p.parser.success = False
    if aux is not None and type(aux) is FUNCTION:
        params = p[3]
        if len(params[1]) == aux.num_param:
            correct = True
            for i,tipo in enumerate(aux.params.values()):
                if tipo == 'real' and params[1][i] == 'entero':
                    params[0][aux.num_param-1-i] += '\tITOF\n'
                    print(f'Warning: El tipo de las expresiones: {params[1][i]} no coincide con el de la variable: {tipo}, esperado para el parametro {list(aux.params.keys())[i]} de la funcion {aux.ID}. lin {p.lexer.lineno}')
                    params[1][i] = 'real'
                correct = correct and tipo == params[1][i]
            s = ''
            for par in params[0]:
                s += par
            params[0] = s
            if correct:
                p[0] = [f'\tPUSHN 1\n{aux.memory}{params[0]}\tPUSHA {aux.ID}\n\tCALL\n\tNOP\n{aux.clean()}',pr.declarations[p[1]].TIPO]
            else:
                print(f'Semantic Error: Los parametros fornecidos: {params[1]}, no tienen el mismo tipo que el esperado: {list(aux.params.values())}. lin {p.lexer.lineno}')
                p[0] = ['','Sin Tipo']
                p.parser.success = False
        else:
            print(f'Semantic Error: El numero de parametros: {len(params[1])}, que la funcion recive no es el esperado: {aux.num_param}. lin {p.lexer.lineno}')
            p[0] = ['','Sin Tipo']
            p.parser.success = False
    else:
        if aux is not None:
            print(f'Semantic Error: El ID {p[1]} no es una funcion')
            p[0] = ['','Sin Tipo']
            p.parser.success = False

def p_fator_exp(p):
    "fator : '(' exp ')'"
    p[0] = p[2]

def p_fator_cast(p):
    "fator : cast"
    p[0] = p[1]

def p_fator_read(p):
    "fator : read"
    p[0] = p[1]

def p_content_paramns_0(p):
    "content_params : "
    p[0] = [[''],[]]

def p_content_paramns_1(p):
    "content_params : list_params"
    p[0] = p[1]

def p_params_function_1(p):
    "list_params : exp"
    p[0] = [[p[1][0]],[p[1][1]]]

def p_params_function_mult(p):
    "list_params : list_params ',' exp"
    p[0] = [[p[3][0]]+p[1][0],p[1][1]+[p[3][1]]]
#------------------------------------------------------

#----------------Conditions----------------------------

def p_conditions_si(p):
    "conditions : SI expL ENTONCES statements endcondition"
    if 'COND' in p[5]:
        p[0] = f'{p[2]}\tJZ {p[5]}\n{p[4]}\nEND{p[5]}: NOP\n'
    else:
        p[0] = f'{p[2]}\tJZ {p[5]}\n{p[4]}\n{p[5]}: NOP\n'

def p_endcpndition(p):
    "endcondition : '.'"
    ID = ID_generator()
    p[0] = 'C'+ID

def p_conditions_si_no(p):
    "endcondition : CASO CONTRARIO statements '.'"
    ID = 'COND'+ID_generator()
    p.parser.program.add_condition(p[3]+f'\tJUMP END{ID}\n',ID)
    p[0] = ID

def p_expL_1(p):
    "expL : termoB"
    p[0] = p[1]

def p_expL_mult(p):
    "expL : expL OR termoB"
    p[0] = f'{p[1]}{p[3]}\tADD\n\tPUSHI 1\n\tSUPEQ\n'

def p_termoB_1(p):
    "termoB : fatorB"
    p[0] = p[1]

def p_termoB_mult(p):
    "termoB : termoB AND fatorB"
    p[0] = f'{p[1]}{p[3]}\tADD\n\tPUSHI 2\n\tEQUAL\n'

def p_fatorB_condition(p):
    "fatorB : condition"
    p[0] = p[1]

def p_fatorB_VERDADERO(p):
    "fatorB : VERDADERO"
    p[0] = '\tPUSHI 1\n'

def p_fatorB_FALSE(p):
    "fatorB : FALSO"
    p[0] = '\tPUSHI 0\n'

def p_fatorB_expL(p):
    "fatorB : '(' expL ')'"
    p[0] = p[1]

def p_condition(p):
    "condition : exp op exp"
    c = operator(p[2],p[1],p[3])
    if c is not None:
        p[0] = f'{c}'
    else:
        print(f'Semantic Error: Las expreciones no son compatibles para la operacion descrita. lin {p.lexer.lineno}')
        p[0] = ''
        p.parser.success = False

def p_op_maior(p):
    "op : '>'"
    p[0] = p[1]

def p_op_menor(p):
    "op : '<'"
    p[0] = p[1]

def p_op_IGUAL(p):
    "op : IGUAL"
    p[0] = '='

def p_op_DIFERENTE(p):
    "op : DIFERENTE"
    p[0] = '!='

def p_op_maiorIGUAL(p):
    "op : '>' IGUAL"
    p[0] = '>='

def p_op_menorIGUAL(p):
    "op : '<' IGUAL"
    p[0] = '<='

#---------------------------------------

#------------Ciclos---------------------

def p_ciclos_while(p):
    "ciclos : ENCUANTO expL HACER statements '.'"
    ID = ID_generator()
    p[0] = f'\nWHILE{ID}: NOP\n{p[2]}\tJZ ENDWHILE{ID}\n{p[4]}\tJUMP WHILE{ID}\n\nENDWHILE{ID}: NOP\n'

def p_ciclos_for_1(p):
    "ciclos : PARA expL SIGUIENTE atrib '.'"
    ID = ID_generator()
    p[0] = f'\nFOR{ID}: NOP\n{p[2]}\tJZ ENDFOR{ID}\n{p[4]}\tJUMP FOR{ID}\n\nENDFOR{ID}: NOP\n'

def p_ciclos_for_mult(p):
    "ciclos : PARA expL SIGUIENTE atrib HACER statements '.'"
    ID = ID_generator()
    p[0] = f'\nFOR{ID}: NOP\n{p[2]}\tJZ ENDFOR{ID}\n{p[6]}{p[4]}\tJUMP FOR{ID}\n\nENDFOR{ID}: NOP\n'


#----------------------------------------

#----------Read and Write---------------

def p_write_r(p):
    "write : ESCRIBIR '(' exp ')' ';'"
    p[0] = f'{p[3][0]}\t{write_f(p[3][1])}\n\tPUSHS "\\n"\n\tWRITES\n'

def p_write_end(p):
    "write : ESCRIBIR '(' exp ',' FIM ':' exp ')' ';'"
    p[0] = f'{p[3][0]}\t{write_f(p[3][1])}\n{p[7][0]}\t{write_f(p[7][1])}\n'

def p_read_w(p):
    "read : LEER '(' exp ')'"
    p[0] = [f'{p[3][0]}\t{write_f(p[3][1])}\n\tREAD\n','string']

#---------------------------------------------

#----------------------CAST--------------------

def p_cast_exp(p):
    "cast : tipocast '(' exp ')'"
    p[0] =  [make_cast(p[3],p[1]),p[1]]

def p_tipocast_float(p):
    "tipocast : REAL"
    p[0] = p[1]

def p_tipocast_int(p):
    "tipocast : ENTERO"
    p[0] = p[1]

def p_tipocast_string(p):
    "tipocast : STR"
    p[0] = p[1]


def p_error(p):
    palabras_reservadas = ["VAR","PARA","SIGUIENTE","ENTERO","REAL","FUNCION","ENCUANTO","DIFERENTE","IGUAL"
          ,"HACER", "DEVUELVE","LISTA","BOOLEANO","SI","RESTO","ENTONCES","VERDADERO","FALSO","CASO","CONTRARIO",
          "AND","OR","LEER","ESCRIBIR","STR","FIM","EXP","LN"]
    if p is None:
        print("Sintax Error: Abrio el comentario pero no fue cerrado")
        parser.success = False
    else:
        col = find_column(p.lexer.lexdata,p.lexpos)
        m = f'{p.value} es una palabra reservada y no es posible ser usada en ese contexto. ' if p.type in palabras_reservadas else ''
        if col > 1 or m != '':
            print(f"Syntax error: {m} lin {p.lineno} col {col}")
        else:
            col = find_column(p.lexer.lexdata,p.lexpos-2)
            print(f"Syntax error: {p.lexer.lexdata[p.lexpos-2]} lin {p.lineno-1} col {col}")
        parser.success = False

parser = yacc.yacc()
parser.program = PROGRAM()
parser.save_program = None
parser.flag_function = False
parser.parameters = []
parser.comp_lista = 0
parser.success = True
parser.cast = False
parser.code = 'START\n'


def parse_compile(content):
    parser.parse(content)
    if parser.success and parser.program.success:
        print("Parsing completed")
        return parser.code
    else:
        print("Error, no fue posible compilar")
        return None


def compile(filename):
    path = 'code_examples/'
    file = open(path+filename,"r")
    content = file.read()
    code=parse_compile(content)
    #print(code)
    if code is not None:
        file_writer.saveFile(filename, path,code )

if __name__ == '__main__':
    compile('test.txt')