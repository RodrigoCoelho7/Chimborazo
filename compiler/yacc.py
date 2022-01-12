import ply.yacc as yacc
from Lex import tokens
import re
from libs.objects import PROGRAM, DECLARATION, FUNCTION
from libs.functions import allocate_memory,operator,ID_generator,write_f,cast,make_cast


def p_prg(p):
    "prg : declarations statements"
    p.parser.code = p.parser.program.memory + p.parser.code + p[1][0] + p[2] + '\tSTOP\n' + p.parser.program.statements_code()

#-------------- Declarations ------------------------------

def p_declarations_1(p):
    "declarations : decl"
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
        print('Error con el tipo en las atribuciones')

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
    p.parser.declarations.append(DECLARATION(p[1],TOKEN='string',memory=p.parser.program.GP))
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

def p_parametros_1(p):
    "parametros : ID ':' tipo"
    if p.parser.save_program is None:
        p.parser.save_program = p.parser.program
        p.parser.program = FUNCTION()
    p.parser.program.set_paramns([DECLARATION(p[1],TIPO=p[3],memory=p.parser.program.GP)])
    p.parser.program.count_pointer()
    p[0] = ''

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
        print(f'Error de tipo verifique a expresion: {p[1]} es {p.parser.program.declarations[p[1]].TIPO} y string')
    
def p_atrib_true(p):
    "atrib : ID '=' VERDADERO"
    if 'booleano' == p.parser.program.declarations[p[1]].TIPO:
        p[0] = f'\tPUSHI 1\n{p.parser.program.get_store(p[1])}'
    else:
        print(f'Error de tipo verifique a expresion: {p[1]} es {p.parser.program.declarations[p[1]].TIPO} y booleano')

def p_atrib_false(p):
    "atrib : ID '=' FALSO"
    if 'booleano' == p.parser.program.declarations[p[1]].TIPO:
        p[0] = f'\tPUSHI 0\n{p.parser.program.get_store(p[1])}'
    else:
        print(f'Error de tipo verifique a expresion: {p[1]} es {p.parser.program.declarations[p[1]].TIPO} y booleano')
def p_atrib(p):
    "atrib : ID '=' exp"
    if p[3][1] == p.parser.program.declarations[p[1]].TIPO:
        p[0] = f'{p[3][0]}{p.parser.program.get_store(p[1])}'
    elif p[3][1] == 'entero' and p.parser.program.declarations[p[1]].TIPO:
        print(f'Warning: El tipo de las expresiones no coincide con el de la variable')
        p[0] = f'{p[3][0]}\tITOF\n{p.parser.program.get_store(p[1])}'
    else:
        print(f'Error de tipo verifique a expresion: {p[1]} es {p.parser.program.declarations[p[1]].TIPO} y {p[3][1]}')
        exit()

def p_exp_soma(p):
    "exp : exp '+' termo"
    code = cast(p[1],p[3])
    p[0] = [f'{code[0]}ADD\n',code[1]]

def p_exp_sub(p):
    "exp : exp '-' termo"
    code = cast(p[1],p[3])
    p[0] = [f'{code[0]}SUB\n',code[1]]

def p_exp_termo(p):
    "exp : termo"
    p[0] = p[1]

def p_termo_mul(p):
    "termo : termo '*' fator"
    code = cast(p[1],p[3])
    p[0] = [f'{code[0]}MUL\n',code[1]]

def p_termo_div(p):
    "termo : termo '/' fator"
    code = cast(p[1],p[3])
    p[0] = [f'{code[0]}DIV\n',code[1]]

def p_termo_pot(p):
    "termo : termo '^' fator"
    if p[3][1] != 'entero':
        print('ERROR: Potencia solamente definida para exponente entero')
        exit()
    if p[1][1] != 'entero' and p[1][1] != 'real':
        print('ERROR: Potencia solamente definida para base entera o real')
        exit()
    c = '' if p[1][1] == 'entero' else 'F'
        
    pot = f'WHILEPOTENCIA: NOP\n\tPUSHL -2\n\tPUSHI 1\n\tSUP\n\tJZ ENDWHILEPOTENCIA\n\tPUSHL -1\n\tPUSHL -1\n\t{c}MUL\n\tSTOREL -1\n\tJUMP WHILEPOTENCIA\n\
ENDWHILEPOTENCIA: NOP\n\tPUSHL -1\n\tSTOREL -3\n\tRETURN\n'
    p.parser.program.add_function(pot,'SYSPOTENCIA')
    p[0] = [f'\tPUSHN 1\n{p[3][0]}{p[1][0]}\tPUSHA SYSPOTENCIA\n\tCALL\n\tNOP\n\tPOP 2\n',p[1][1]]

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

def p_fator_ID(p):
    "fator : ID"
    p[0] = [p.parser.program.get_push(p[1]),p.parser.program.declarations[p[1]].TIPO]

def p_fator_FUNC(p):
    "fator : ID '(' content_params ')' "
    aux = p.parser.program.declarations[p[1]]
    if type(aux) is FUNCTION:
        params = p[3]
        if len(params[1]) == aux.num_param:
            correct = True
            for i,tipo in enumerate(aux.params.values()):
                correct = correct and tipo == params[1][i]
            if correct:
                p[0] = [f'\tPUSHN 1\n{aux.memory}{params[0]}\tPUSHA {aux.ID}\n\tCALL\n\tNOP\n{aux.clean()}',p.parser.program.declarations[p[1]].TIPO]
            else:
                print(f'Error: Los parametros fornecidos no tienen el mismo tipo que el esperado. {params[1]}, {list(aux.params.values())}')
                exit()
        else:
            print(f'Error: El numero de parametros que la funcion recive no es el esperado, {len(params[1])}, {aux.num_param}')
            exit()

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
    p[0] = ['',[]]

def p_content_paramns_0(p):
    "content_params : list_params"
    p[0] = p[1]

def p_params_function_1(p):
    "list_params : exp"
    p[0] = [p[1][0],[p[1][1]]]

def p_params_function_mult(p):
    "list_params : list_params ',' exp"
    p[0] = [p[3][0]+p[1][0],p[1][1]+[p[3][1]]]
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
    p[0] = f'{operator(p[2],p[1],p[3])}'

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
    "write : ESCRIBIR '(' ID ')' ';'"
    p[0] = f'{p.parser.program.get_push(p[3])}\t{write_f(p.parser.program.declarations[p[3]].TIPO)}\n'

def p_write_r_string(p):
    "write : ESCRIBIR '(' STRING ')' ';'"
    p[0] = f'\tPUSHS {p[3]}\n\tWRITES\n'

def p_read_w(p):
    "read : LEER '(' STRING ')'"
    p[0] = [f'\tPUSHS {p[3]}\n\tWRITES\n\tREAD\n','string']

#---------------------------------------------

#----------------------CAST--------------------

def p_cast_exp(p):
    "cast : tipocast '(' exp ')'"
    p[0] =  [make_cast(p[3],p[1]),p[1]]

def p_cast_string(p):
    "cast : tipocast '(' STRING ')'"
    p[0] = [make_cast(p[3],p[1]),p[1]]

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
    print("Syntax error!",p)
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

path = 'code_examples/'
file = open(path+"funcion_potencia.txt","r")
content = file.read()

parser.parse(content)
if parser.success == True:
    print("Parsing completed")
    print(parser.code)