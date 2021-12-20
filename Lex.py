import ply.lex as lex

tokens = ["VAR","PARA","SIGUIENTE","ENTERO","REAL","FUNCION","ENCUANTO","DIFERENTE","IGUAL","NADA"
          ,"HACER", "DEVUELVE","LISTA","BOOLEANO","SI","RESTO","ENTONCES","ESCRIBE","VERDADERO","FALSO","NO",
          "FLOAT","INT","ID","TAB","ENTER","STRING"]

literals = [",",":","=","<",">","+","-","*","/",".","(",")","[","]","'","^","O","y"]

def t_STRING(t):
    r'\"[^"]*\"'
    return t

def t_ENTER(t):
    r'\n'
    return t

def t_TAB(t):
    r'\t|^\s{4}'
    return t

def t_SPACE(t):
    r'\s'

def t_VAR(t):
    r'\bvariable\b'
    return t

def t_PARA(t):
    r'\bpara\b'
    return t

def t_SIGUIENTE(t):
    r'\bsiguiente\b'
    return t

def t_ENTERO(t):
    r'\bentero\b'
    return t

def t_REAL(t):
    r'\breal\b'
    return t

def t_FUNCION(t):
    r'\bfuncion\b'
    return t

def t_ENCUANTO(t):
    r'\bencuanto\b'
    return t

def t_DIFERENTE(t):
    r'\bdiferente\b'
    return t

def t_IGUAL(t):
    r'\bigual\b'
    return t

def t_NADA(t):
    r'\bnada\b'
    return t

def t_HACER(t):
    r'\bhacer\b'
    return t

def t_LISTA(t):
    r'\blista\b'
    return t

def t_DEVUELVE(t):
    r'\bdevuelve\b'
    return t

def t_BOOLEANO(t):
    r'\bbooleano\b'
    return t

def t_SI(t):
    r'\bsi\b'
    return t

def t_RESTO(t):
    r'\bresto\b'
    return t

def t_ENTONCES(t):
    r'\bentonces\b'
    return t

def t_ESCRIBE(t):
    r'\bescribe\b'
    return t

def t_VERDADERO(t):
    r'\bVerdadero\b'
    return t

def t_FALSO(t):
    r'\bFalso\b'
    return t

def t_NO(t):
    r'\bno\b'
    return t

def t_FLOAT(t):
    r'([1-9][0-9]*\.[0-9]+|0\.[0-9]+)'
    return t

def t_INT(t):
    r'[1-9][0-9]*|0'
    return t

def t_ID(t):
    r'[a-zA-Z]+\w*'
    return t


def t_error(t):
    print("Caracter ilegal!",t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

'''file = open('Exemplos.txt', 'r')
contents = file.read()

lexer.input(contents)
tok = lexer.token()
while tok:
    print(tok)
    tok = lexer.token()


import sys

for line in sys.stdin:
    lexer.input(line)
    for tok in lexer:
        print(tok)'''