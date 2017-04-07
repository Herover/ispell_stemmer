

import ply.lex as lex
import re
import codecs

class ispell:

    flags = {}
    lexer = False
    wordrelations = {}

    def __init__(self):
        from .ispell_tokrules import ispell_tokrules
        self.lexer = ispell_tokrules()
        self.lexer.build()

    def readAffixFile(self, filename):
        with codecs.open(filename,
                         "r", encoding="utf-8",
                         errors="backslashreplace") as input_file:
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
                    self.flags[flag].append(
                        (cond.lower(), strip.lower(), append.lower())
                    )
    
    def readWordFile(self, filename, encoding = "utf-8"):
        with codecs.open(filename,
                         "r",
                         encoding = encoding,
                         errors="backslashreplace"
        ) as input_file:
            while True:
                line = input_file.readline()
                if line == "":
                    break
                line = line[:-1] # remove \n
                parts = re.split(r'\/', line)
                if len(parts) == 2:
                    for c in parts[1]:
                        for cond in self.flags[c]:
                            if not cond[0].startswith("[") and (cond[0] == "." or parts[0].lower().endswith(cond[0])):
                                part = parts[0] # TODO: naming
                                part = part.lower()
                                if cond[1] != "":
                                    remove = cond[1][1:]
                                    # TODO: Fail or warn if remove is not the end of part
                                    part = part[0:len(part) - len(remove)]
                                self.insertWordRelation(part + cond[2], parts[0].lower())
                            elif cond[0].startswith("["):
                                chars = cond[0][1:-1]
                                endswith = True
                                if chars.startswith("^"):
                                    endswith = False
                                    chars = chars[1:]
                                for char in chars:
                                    if parts[0].lower().endswith(char) == endswith:
                                        self.insertWordRelation(parts[0].lower() + cond[2], parts[0].lower())
                # Insert baseword and word without flags
                self.insertWordRelation(parts[0].lower(), parts[0].lower())

    def insertWordRelation(self, word, baseword):
        if word in self.wordrelations:
            # Test if we have already inserted this relation
            try:
                self.wordrelations[word].index(baseword)
            except:
                self.wordrelations[word].append(baseword)
        else:
            self.wordrelations[word] = [baseword]
    
    def getBaseOfWord(self, word):
        if word in self.wordrelations:
            return self.wordrelations[word]
        else:
            return None

