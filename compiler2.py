import sys
sys.path.append('compiler/')
import yacc
if __name__ == '__main__':
    filename= "cuadrado.txt"
    yacc.compile(filename)
