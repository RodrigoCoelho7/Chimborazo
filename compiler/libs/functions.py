import re
from time import time_ns
import numpy as np

CHARS = [chr(i) for i in range(65,91)]

def allocate_memory(N,TIPO):
    if TIPO == 'real':
        return f'\tPUSHF 0.0\n'*N
    return f'\tPUSHN {N}\n'
    
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

def operator(op,exp1,exp2,program):
    f = F(exp1,exp2,program)
    if op == '=':
        return f'\tEQUAL\n'
    if op == '!=':
        return f'\tEQUAL\tNOT\n'
    if op == '<':
        return f'\t{f}INF\n'
    if op == '>':
        return f'\t{f}SUP\n'
    if op == '<=':
        return f'\t{f}INFEQ\n'
    if op == '>=':
        return f'\t{f}SUPFEQ\n'
    
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