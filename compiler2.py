import sys
sys.path.append('compiler/')
import yacc
if __name__ == '__main__':
    filename= sys.argv[1]
    yacc.compile(filename)
