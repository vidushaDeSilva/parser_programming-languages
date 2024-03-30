class lex:
    def __init__(self, input):
        self.input = input
        self.pos = 0
        self.operator_symbol = ['+', '-', '*', '/', '(', ')', '{', '}', '[', ']', ';', ',', '<', '>', '=', '!', '&', '|']
        self.digits = '0123456789'
        self.punctuation = ['(', ')', ';', ',']
        self.tokens = []

    def lex(self):
        while self.pos < len(self.input):
            if self.input[self.pos] in self.digits:
                self.tokenize_INTEGERS()
            elif self.input[self.pos] in self.operator_symbol:
                self.tokens.append(['OPERATOR', self.input[self.pos]])
                self.pos += 1
            elif self.input[self.pos] in self.punctuation:
                self.tokens.append(['PUNCTUATION', self.input[self.pos]])
                self.pos += 1
            elif self.input[self.pos].isalpha():
                self.tokenize_ID()
            elif self.input[self.pos] == '"':
                self.tokenize_STRING()
            elif self.input[self.pos] == ' ':
                self.tokenize_DELETE_space()
            elif self.input[self.pos] == '/*':
                self.tokenize_DELETE_comments()
            else:
                self.illegalCharError(self.input[self.pos])
                self.pos += 1

        return self.tokens

    def tokenize_INTEGERS(self):
        token = self.input[self.pos]
        self.pos += 1
        while self.pos < len(self.input) and self.input[self.pos] in self.digits:
            token += self.input[self.pos]
            self.pos += 1
        self.tokens.append(('INTEGER', token))
            
    def tokenize_ID(self):
        token = self.input[self.pos]
        self.pos += 1
        while self.pos < len(self.input) and self.input[self.pos].isalpha():
            token += self.input[self.pos]
            self.pos += 1
        self.tokens.append(('IDENTIFIER', token))

    def tokenize_STRING(self):
        token = self.input[self.pos]
        self.pos += 1
        while self.pos < len(self.input) and self.input[self.pos] != '"':
            token += self.input[self.pos]
            self.pos += 1
        token += self.input[self.pos]
        self.tokens.append(('STRING', token))

    def tokenize_DELETE_space(self):
        token = self.input[self.pos]
        self.pos += 1
        while self.pos < len(self.input) and self.input[self.pos] == ' ':
            token += self.input[self.pos]
            self.pos += 1
        self.tokens.append(('DELETE', token))

    def tokenize_DELETE_comments(self):
        token = self.input[self.pos]
        self.pos += 1
        while self.pos < len(self.input) and self.input[self.pos] != '*/':
            token += self.input[self.pos]
            self.pos += 1
        token += self.input[self.pos]
        self.tokens.append(('DELETE', token))

    def illegalCharError(self, char):
         print(char+" is an illegal character")

lexer = lex("sas136*        123")
tokens = lexer.lex()
print(tokens)