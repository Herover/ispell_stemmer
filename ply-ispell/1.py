
flags = {}
curflag = "UNKNOWN"

import ply.lex as lex
import re
import codecs

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
    r'flag\s\*'
    t.lexer.begin('flag')

#t_flag_COLLON = r'\:'
def t_flag_COLLON(t):
    r'\:\n'
    pass

def t_flag_NAME(t):
    r'[a-zA-Z]'
    #print("flag name", t)
    #t.lexer.begin('INITIAL')
    flags[t.value] = []
    flags["curflag"] = t.value
    curflag = t.value # ??
    return t

# TODO: Turn each "field" into token?
def t_flag_CONDITION(t):
    r'[\t\s]+.+[\t\s]+\>[\t\s].+\n'
    split = re.split(r'[\t\s]+', t.value)
    cond = split[1]
    append = split[3]
    appendsplit = re.split(r'\,', append)
    strip = ""
    if not len(appendsplit) == 1:
        append = appendsplit[1]
        strip = appendsplit[0]
    flags[flags["curflag"]].append((cond.lower(), strip.lower(), append.lower()))
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


lexer = lex.lex()

with codecs.open("../corpa/ispell/dansk.aff", "r", encoding="utf-8", errors="backslashreplace") as input_file:
    content = input_file.read()
    
    lexer.input(content)
    while True:
        tok = lexer.token()
        if not tok:
            break
        # TODO: Move some logic from lexer to here
        # print(tok)

thelist = {}
with codecs.open("../corpa/ispell/dansk.ispell", "r", encoding="utf-8", errors="backslashreplace") as input_file:
    while True:
        line = input_file.readline()
        if line == "":
            break
        line = line[:-1] # remove \n
        parts = re.split(r'\/', line)
        if len(parts) == 2:
            for c in parts[1]:
                for cond in flags[c]:
                    # print(parts[0], cond[0])
                    if parts[0].lower().endswith(cond[0]):
                        # print(cond)
                        if cond[1] == "":
                            thelist[parts[0] + cond[2]] = parts[0]
        
        thelist[parts[0]] = parts[0]
        
from collections import OrderedDict
orderedlist = OrderedDict(sorted(thelist.items()))
print(orderedlist)

    

