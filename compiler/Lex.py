import ply.lex as lex

tokens = ["VAR","PARA","SIGUIENTE","ENTERO","REAL","FUNCION","ENCUANTO","DIFERENTE","IGUAL","NADA"
          ,"HACER", "DEVUELVE","LISTA","BOOLEANO","SI","RESTO","ENTONCES","VERDADERO","FALSO","CASO","CONTRARIO",
          "FLOAT","INT","ID","STRING","AND","OR","ENTER","LEER","ESCRIBIR","STR"]

literals = [",",":","=","<",">","+","-","*","/",".","(",")","[","]","'","^",";"]

def find_column(input, pos):
    line_start = input.rfind('\n', 0, pos) + 1
    return (pos - line_start) + 1

def t_STR(t):
    r'\bstring\b'
    return t

def t_LEER(t):
    r'\blee\b'
    return t

def t_ESCRIBIR(t):
    r'\bescribe\b'
    return t

def t_STRING(t):
    r'\"[^"]*\"'
    return t

def t_OR(t):
    r'O'
    return t

def t_AND(t):
    r'Y'
    return t

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

def t_VERDADERO(t):
    r'\bVerdadero\b'
    return t

def t_FALSO(t):
    r'\bFalso\b'
    return t

def t_CASO(t):
    r'\bcaso\b'
    return t

def t_CONTRARIO(t):
    r'\bcontrario\b'
    return t

def t_FLOAT(t):
    r'([1-9][0-9]*\.[0-9]+|0\.[0-9]+)'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'[1-9][0-9]*|0'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z]+\w*'
    return t

def t_ENTER(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Caracter ilegal: {t.value[0]} en la posicion: lin {t.lineno} col {find_column(t.lexer.lexdata,t.lexpos)}")
    t.lexer.skip(1)

t_ignore = " \t"

lexer = lex.lex()

if __name__ == '__main__':
    path = 'code_examples/'
    file = open(path+"cuadrado.txt","r")
    contents = file.read()

    lexer.input(contents)
    tok = lexer.token()
    while tok:
        print(tok)
        tok = lexer.token()