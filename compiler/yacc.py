import ply.yacc as yacc
from Lex import tokens
from libs.objects import PROGRAM, DECLARATION, FUNCTION


def p_prg(p):
    "prg : declarations statements"
    parser.code += 'STOP'

#-------------- Declarations ------------------------------

def p_declarations_1(p):
    "declarations : decl"
    if not p.parser.flag_function:
        for decl in p.parser.declarations:
            p.parser.program.add_variable(decl)
        p.parser.declarations = []

def p_declarations_mult(p):
    "declarations : declarations decl"
    if not p.parser.flag_function:
        for decl in p.parser.declarations:
            p.parser.program.add_variable(decl)
        p.parser.declarations = []

def p_decl_V(p):
    "decl : declV"
    p[0] = p[1]

def p_decl_F(p):
    "decl : declF"

def p_decl_L(p):
    "decl : declL"

#---------------------------------------------------------------

#----------------- Variable declarations ----------------------------

def p_declV(p):
    "declV : VAR ids ':' tipo"
    for var in p.parser.declarations:
        var.set_tipo(p[4])

def p_ids_1(p):
    "ids : ID"
    p.parser.declarations.append(DECLARATION(p[1]))

def p_ids_mult(p):
    "ids : ids ',' ID"
    p.parser.declarations.append(DECLARATION(p[3]))

def p_tipo_int(p):
    "tipo : ENTERO"
    p[0]= p[1]

def p_tipo_REAL(p):
    "tipo : REAL"
    p[0] = p[1]

def p_tipo_BOOL(p):
    "tipo : BOOLEANO"
    p[0] = p[1]

#------------------------------------------------------

#-----------------List Declarations --------------------------

def p_declL(p):
    "declL : LISTA ID '=' lista"
    p.parser.declarations.append(DECLARATION(p[4],"lista"))
    p[0] = p[1] + ' ' + p[2] + p[3] + p[4]
    print(p[0])

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
    f = FUNCTION(p[2],p[7],p.parser.parameters,p.parser.return_tipo)
    p.parser.return_tipo = None
    for decl in p.parser.declarations:
        f.add_variable(decl)
    f.valida_tipo()
    p.parser.declarations = [f]
    p.parser.flag_function = False
    p.parser.parameters = []
    
def p_parametros_0(p):
    "parametros : "

def p_parametros_1(p):
    "parametros : ID ':' tipo"
    p.parser.flag_function = True
    p.parser.parameters.append(DECLARATION(p[1],TIPO=p[3]))

def p_parametros_mult(p):
    "parametros : parametros ',' ID ':' tipo"
    p.parser.flag_function = True
    p.parser.parameters.append(DECLARATION(p[3],TIPO=p[5]))

def p_return_INT(p):
    "return : INT"
    p.parser.return_tipo = ('entero',p[1])

def p_return_ID(p):
    "return : ID"
    p.parser.return_tipo = ('ID',p[1])

def p_return_FLOAT(p):
    "return : FLOAT"
    p.parser.return_tipo = ('real',p[1])

def p_return_TRUE(p):
    "return : VERDADERO"
    p.parser.return_tipo = ('booleano',p[1])

def p_return_FALSE(p):
    "return : FALSO"
    p.parser.return_tipo = ('booleano',p[1])

#----------------------------------------------------------------------------

#----------------------STATEMENTS-------------------------------------------

def p_statements_1(p):
    "statements : stat"

def p_statements_mult(p):
    "statements : statements stat"

def p_stat_atrib(p):
    "stat : atrib ';'"

def p_stat_conditions(p):
    "stat : conditions"

def p_stat_ciclos(p):
    "stat : ciclos"

#-----------------ATRIBUIÇÕES-------------------------

def p_atrib(p):
    "atrib : ID '=' exp"
    p[0] = p[3]

def p_exp_soma(p):
    "exp : exp '+' termo"
    p[0] = p[1] + p[3]

def p_exp_sub(p):
    "exp : exp '-' termo"
    p[0] = p[1] - p[3]

def p_exp_termo(p):
    "exp : termo"
    p[0] = p[1]

def p_termo_mul(p):
    "termo : termo '*' fator"
    p[0] = p[1] * p[3]

def p_termo_div(p):
    "termo : termo '/' fator"
    p[0] = p[1] / p[3]

def p_termo_pot(p):
    "termo : termo '^' fator"
    p[0] = p[1] ** p[3]

def p_termo_fator(p):
    "termo : fator"
    p[0] = p[1]

def p_fator_INT(p):
    "fator : INT"
    p[0] = p[1]

def p_fator_FLOAT(p):
    "fator : FLOAT"
    p[0] = p[1]

def p_fator_ID(p):
    "fator : ID"
    p[0] = p[1]

def p_fator_exp(p):
    "fator : '(' exp ')'"
    p[0] = p[2]

#------------------------------------------------------

#----------------Conditions----------------------------

def p_conditions_si(p):
    "conditions : SI expL ENTONCES statements endcondition"

def p_endcpndition(p):
    "endcondition : '.'"

def p_conditions_si_no(p):
    "endcondition : CASO CONTRARIO statements '.'"

def p_expL_1(p):
    "expL : termoB"

def p_expL_mult(p):
    "expL : expL OR termoB"

def p_termoB_1(p):
    "termoB : fatorB"

def p_termoB_mult(p):
    "termoB : termoB AND fatorB"

def p_fatorB_condition(p):
    "fatorB : condition"

def p_fatorB_BOOL(p):
    "fatorB : BOOLEANO"

def p_fatorB_expL(p):
    "fatorB : '(' expL ')'"

def p_condition(p):
    "condition : exp op exp"

def p_op_maior(p):
    "op : '>'"

def p_op_menor(p):
    "op : '<'"

def p_op_IGUAL(p):
    "op : IGUAL"

def p_op_DIFERENTE(p):
    "op : DIFERENTE"

def p_op_maiorIGUAL(p):
    "op : '>' IGUAL"

def p_op_menorIGUAL(p):
    "op : '<' IGUAL"

#---------------------------------------

#------------Ciclos---------------------

def p_ciclos_while(p):
    " ciclos : ENCUANTO expL HACER statements '.'"

def p_ciclos_for_1(p):
    "ciclos : PARA expL SIGUIENTE atrib '.'"

def p_ciclos_for_mult(p):
    "ciclos : PARA expL SIGUIENTE atrib HACER statements '.'"

def p_error(p):
    print("Syntax error!",p)
    parser.success = False

parser = yacc.yacc()
parser.program = PROGRAM()
parser.flag_function = False
parser.declarations = []
parser.parameters = []
parser.comp_lista = 0
parser.success = True
parser.code = 'START\n'

path = 'code_examples/'
file = open(path+"cuadrado.txt","r")
content = file.read()

parser.parse(content)
if parser.success == True:
    print("Parsing completed")
