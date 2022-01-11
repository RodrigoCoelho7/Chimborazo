import re
from time import time_ns
import numpy as np

CHARS = [chr(i) for i in range(65,91)]

def allocate_memory(N,TIPO):
    if TIPO == 'real':
        return f'\tPUSHF 0.0\n'*N
    return f'\tPUSHN {N}\n'

def cast(exp1,exp2):
    if exp1[1] == 'real' and exp2[1] == 'real':
        return [f'{exp1[0]}{exp2[0]}\tF','real']
    if exp1[1] == 'real' and exp2[1] == 'entero':
        print(f'Warning: El tipo de las expresiones no coincide {exp1[1]} {exp2[1]}')
        return [f'{exp1[0]}{exp2[0]}\tITOF\n\tF','real']
    if exp1[1] == 'entero' and exp2[1] == 'real':
        print(f'Warning: El tipo de las expresiones no coincide {exp1[1]} {exp2[1]}')
        return [f'{exp1[0]}\tITOF\n{exp2[0]}\tF','real']
    if exp1[1] == 'entero' and exp2[1] == 'entero':
        return [f'{exp1[0]}{exp2[0]}\t','entero']
    return None

def F(exp1,exp2,program):
    if 'PUSHF' in exp1 + exp2:
        return 'F'
    if 'PUSHG' in exp1 + exp2:
        pointers = re.finditer(r'PUSHG (\d+)',exp1+exp2)
        for m in pointers:
            var = program.get_Variable_by_memory(int(m.group(1)))
            if var:
                if program.declarations[var].TIPO == 'real':
                    return 'F'
    return ''

def operator(op,exp1,exp2):
    f = cast(exp1,exp2)[0]
    if op == '=':
        return f'{f[:-1]}EQUAL\n'
    if op == '!=':
        return f'{f[:-1]}EQUAL\tNOT\n'
    if op == '<':
        return f'{f}INF\n'
    if op == '>':
        return f'{f}SUP\n'
    if op == '<=':
        return f'{f}INFEQ\n'
    if op == '>=':
        return f'{f}SUPFEQ\n'
    
def ID_generator():
    np.random.shuffle(CHARS)
    time_code = str(time_ns())[10:17]
    ID = time_code[:2]+CHARS[int(time_code[3])]+CHARS[int(time_code[4])]+time_code[5:]
    return ID

def write_f(tipo):
    if tipo == 'string':
        return 'WRITES'
    if tipo == 'real':
        return 'WRITEF'
    if tipo == 'entero':
        return 'WRITEI'
    if tipo == 'booleano':
        return 'WRITEI'

def make_cast(exp,tipo):
    if tipo == 'string' and exp[1] != 'string':
        fr = 'I' if exp[1] == 'entero' or exp[1] == 'booleano' else 'F'
        return f'{exp[0]}\tSTR{fr}\n'
    if tipo == 'real' and exp[1] != 'real':
        fr = 'I' if exp[1] == 'entero' or exp[1] == 'booleano' else 'A'
        return f'{exp[0]}\t{fr}TOF\n'
    if tipo == 'entero' and exp[1] != 'entero' and exp[1] != 'booleano':
        fr = 'F' if exp[1] == 'real' else 'A'
        return f'{exp[0]}\t{fr}TOI\n'
    return f'{exp[0]}'
    