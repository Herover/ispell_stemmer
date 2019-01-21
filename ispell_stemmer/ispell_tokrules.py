import ply.lex as lex

class ispell_tokrules():
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
    
    def t_FLAG(self, t):
        #r'(?<=flag\s\*)[a-zA-Z](?=\:\n)'
        r'flag\s'
        t.lexer.begin('flag')
        
    #t_flag_COLLON = r'\:'
    def t_flag_COLLON(self, t):
        r'\:\n'
        pass
        
    def t_flag_NAME(self, t):
        r'\*{0,1}[a-zA-Z]'
        if t.value.startswith("*"):
            t.value = t.value[1:]
        return t
        
    # TODO: Turn each "field" into token?
    def t_flag_CONDITION(self, t):
        r'[\t\s]+.+[\t\s]+\>[\t\s].+\n'
        return t
        
    def t_flag_BLANK(self, t):
        r'\n'
        t.lexer.begin('INITIAL')
        pass
        
    def t_flag_error(self, t):
        print("Warning: Illegal character '%s' ignored" % t.value[0])
        t.lexer.skip(1)
        
    def t_flag_COMMENT(self, t):
        r'\#.*\n'
        pass
        
    def t_SUFFIXES(self, t):
        r'suffixes'
        return t
        
    def t_PREFIXES(self, t):
        r'prefixes'
        return t
    
    def t_SETTING(self, t):
        r'[a-z]+[\s\t]+.+'
        return t
    
    def t_BLANK(self, t):
        r'\n'
        pass
    
    def t_COMMENT(self, t):
        r'\#.*\n'
        pass
    
    def t_eof(self, t):
        return None
    
    def t_error(self, t):
        print("Warning: Illegal character '%s' ignored" % t.value[0])
        t.lexer.skip(1)
    
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def input(self, content):
        return self.lexer.input(content)

    def token(self):
        return self.lexer.token()
