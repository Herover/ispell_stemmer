

import ply.lex as lex
import re
import codecs

class ispell:

    flags = {}
    lexer = False

    def __init__(self):
        import ispell_tokrules
        self.lexer = lex.lex(ispell_tokrules)

    def readAffixFile(self, filename):
        with codecs.open(filename, "r", encoding="utf-8", errors="backslashreplace") as input_file:
            content = input_file.read()

            flag = ""    
            self.lexer.input(content)
            while True:
                tok = self.lexer.token()
                if not tok:
                    break
                # TODO: Move some logic from lexer to here
                if tok.type == "NAME":
                    flag = tok.value
                    self.flags[flag] = []
                elif tok.type == "CONDITION":
                    split = re.split(r'[\t\s]+', tok.value)
                    cond = split[1]
                    append = split[3]
                    appendsplit = re.split(r'\,', append)
                    strip = ""
                    if not len(appendsplit) == 1:
                        append = appendsplit[1]
                        strip = appendsplit[0]
                    self.flags[flag].append((cond.lower(), strip.lower(), append.lower()))
            #print(flags)
    def readWordFile(self, filename):
        thelist = {}
        with codecs.open(filename, "r", encoding="utf-8", errors="backslashreplace") as input_file:
            while True:
                line = input_file.readline()
                if line == "":
                    break
                line = line[:-1] # remove \n
                parts = re.split(r'\/', line)
                if len(parts) == 2:
                    for c in parts[1]:
                        for cond in self.flags[c]:
                            # print(parts[0], cond[0])
                            if parts[0].lower().endswith(cond[0]):
                                # print(cond)
                                if cond[1] == "":
                                    thelist[parts[0] + cond[2]] = parts[0]
        
            thelist[parts[0]] = parts[0]
        
            from collections import OrderedDict
            orderedlist = OrderedDict(sorted(thelist.items()))
            print(orderedlist)


test = ispell()
test.readAffixFile("../corpa/ispell/dansk.aff")
test.readWordFile("../corpa/ispell/dansk.ispell")
