

import ply.lex as lex
import re
import codecs

import ispell_tokrules
lexer = lex.lex(ispell_tokrules)

with codecs.open("../corpa/ispell/dansk.aff", "r", encoding="utf-8", errors="backslashreplace") as input_file:
    content = input_file.read()

    flags = {}
    flag = ""
    
    lexer.input(content)
    while True:
        tok = lexer.token()
        if not tok:
            break
        # TODO: Move some logic from lexer to here
        if tok.type == "NAME":
            flag = tok.value
            flags[flag] = []
        elif tok.type == "CONDITION":
            split = re.split(r'[\t\s]+', tok.value)
            cond = split[1]
            append = split[3]
            appendsplit = re.split(r'\,', append)
            strip = ""
            if not len(appendsplit) == 1:
                append = appendsplit[1]
                strip = appendsplit[0]
            flags[flag].append((cond.lower(), strip.lower(), append.lower()))
    #print(flags)

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

    

