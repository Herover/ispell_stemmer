tokens = (
    'FLAG',
    'NAME',
    'COLLON',
    'CONDITION',
    'BLANK',
    'SETTING',
    'SUFFIXES',
    'PREFIXES'
#    "SUFFIX",
#    "PREFIX",
#    "SETTING",
)

states = (
    ('flag', 'exclusive'),
)

t_ignore = ""
#t_flag_ignore = "\n"

def t_FLAG(t):
    #r'(?<=flag\s\*)[a-zA-Z](?=\:\n)'
    r'flag\s'
    t.lexer.begin('flag')

#t_flag_COLLON = r'\:'
def t_flag_COLLON(t):
    r'\:\n'
    pass

def t_flag_NAME(t):
    r'\*{0,1}[a-zA-Z]'
    if t.value.startswith("*"):
        t.value = t.value[1:]
    return t

# TODO: Turn each "field" into token?
def t_flag_CONDITION(t):
    r'[\t\s]+.+[\t\s]+\>[\t\s].+\n'
    return t

def t_flag_BLANK(t):
    r'\n'
    t.lexer.begin('INITIAL')
    pass

def t_flag_error(t):
    print("Warning: Illegal character '%s' ignored" % t.value[0])
    t.lexer.skip(1)

def t_flag_COMMENT(t):
    r'\#.*\n'
    pass

def t_SUFFIXES(t):
    r'suffixes'
    return t

def t_PREFIXES(t):
    r'prefixes'
    return t

def t_SETTING(t):
    r'[a-z]+[\s\t]+.+'
    return t

def t_BLANK(t):
    r'\n'
    pass

def t_COMMENT(t):
    r'\#.*\n'
    pass

def t_eof(t):
    return None

def t_error(t):
    print("Warning: Illegal character '%s' ignored" % t.value[0])
    t.lexer.skip(1)

#def t_error(t):
