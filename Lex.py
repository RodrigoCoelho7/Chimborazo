import ply.lex as lex

tokens = ["VAR","PARA","SIGUIENTE","ENTERO","REAL","FUNCION","ENQUANTO","DIFERENTE","IGUAL","NADA"
          ,"HACER", "DEVUELVE","LISTA","BOOLEANO","SI","RESTO","ENTONCES","ESCRIBE","VERDADERO","FALSO","NO",
          "FLOAT","INT","ID","SPACE","TAB","ENTER","STRING"]

literals = [",",":","=","<",">","+","-","*","/",".","(",")","[","]","'"]

def t_STRING(t):
    r'\"[^"]*\"'
    return t

def t_ENTER(t):
    r'\n'
    return t

def t_TAB(t):
    r'\s{4}'
    return t

def t_SPACE(t):
    '\s'
    return t

def t_VAR(t):
    r'variable'
    return t

def t_PARA(t):
    r'para'
    return t

def t_SIGUIENTE(t):
    r'siguiente'
    return t

def t_ENTERO(t):
    r'entero'
    return t

def t_REAL(t):
    r'real'
    return t

def t_FUNCION(t):
    r'funcion'
    return t

def t_ENQUANTO(t):
    r'enquanto'
    return t

def t_DIFERENTE(t):
    r'diferente'
    return t

def t_IGUAL(t):
    r'igual'
    return t

def t_NADA(t):
    r'nada'
    return t

def t_HACER(t):
    r'hacer'
    return t

def t_LISTA(t):
    r'lista'
    return t

def t_DEVUELVE(t):
    r'devuelve'
    return t

def t_BOOLEANO(t):
    r'booleano'
    return t

def t_SI(t):
    r'si'
    return t

def t_RESTO(t):
    r'resto'
    return t

def t_ENTONCES(t):
    r'entonces'
    return t

def t_ESCRIBE(t):
    r'escribe'
    return t

def t_VERDADERO(t):
    r'Verdadero'
    return t

def t_FALSO(t):
    r'Falso'
    return t

def t_NO(t):
    r'no'
    return t

def t_FLOAT(t):
    r'[0-9]+\.[0-9]+'
    return t

def t_INT(t):
    r'[0-9]+'
    return t

def t_ID(t):
    r'[a-zA-Z]+\w*'
    return t

def t_error(t):
    print("Caracter ilegal!",t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

file = open('Exemplos.txt', 'r')
contents = file.read()

lexer.input(contents)
tok = lexer.token()
while tok:
    print(tok)
    tok = lexer.token()
