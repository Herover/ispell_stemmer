
flags = {}

import ply.lex as lex

tokens = (
    'FLAG',
    'NAME',
    'COLLON',
    '
#    "SUFFIX",
#    "PREFIX",
#    "SETTING",
)

states = (
    ('flag', 'exclusive'),
)

#t_flag_COLLON = r'\:'
def t_flag_COLLON(t):
    r'\:\n'
    pass

def t_FLAG(t):
    #r'(?<=flag\s\*)[a-zA-Z](?=\:\n)'
    r'flag\s\*'
    t.lexer.begin('flag')

def t_flag_NAME(t):
    r'[a-zA-Z]'
    #print("flag name", t)
    #t.lexer.begin('INITIAL')
    return t

def t_COMMENT(t):
    r'\#.*'
    pass

def t_eof(t):
    return None

#def t_error(t):


lexer = lex.lex()

with open("test.aff", "r") as input_file:
    content = input_file.read()
    
    lexer.input(content)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
