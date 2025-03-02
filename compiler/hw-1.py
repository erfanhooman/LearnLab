tokens = ('NUMBER', 'PLUS', 'MUL', 'SUB')

t_PLUS = r'\+'
t_MUL = r'\*'
t_SUB = r'\-'
t_ignore = ' \t'

def t_NUMBER(t):
    r'[0-9]+'
    return int(t.value)

from ply import lex

lex.lex()

"""
s -> E
E -> E + a
E -> E - a
E -> E * a
E -> a
"""

def p_start(p):
    'S : E'
    print("S -> E", p[1])

def p_plus(p):
    'E : E PLUS NUMBER'
    p[0] = p[1] + p[2]

def p_sub(p):
    'E : E SUB NUMBER'
    p[0] = p[1] - p[2]

def p_mul(p):
    'E : E MUL NUMBER'
    p[0] = p[1] * p[2]

def p_number(p):
    'E : NUMBER'
    p[0] = p[1]
