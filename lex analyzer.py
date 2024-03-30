class lex:
    def __init__(self, input):
        self.input = input
        self.pos = -1
        self.current_char = None
        self.operator_symbol = ['+', '-', '*', '/', '(', ')', '{', '}', '[', ']', ';', ',', '<', '>', '=', '!', '&', '|']
        self.digits = '0123456789'
        self.punctuation = ['(', ')', ';', ',']
        self.tokens = []

            
    def lex(self):
        while self.pos < len(self.input):
            if self.input[self.pos] in self.digits:
                self.tokenize_INTEGERS()
            elif self.input[self.pos] in self.ops:
                self.token.append(['OPERATOR', self.input[self.pos]])
            elif self.input[self.pos] in self.punctuation:
                if self.input[self.pos] == '(':
                    self.token.append(['LPAREN', self.input[self.pos]])
                elif self.input[self.pos] == ')':
                    self.token.append(['RPAREN', self.input[self.pos]])
                elif self.input[self.pos] == ';':
                    self.token.append(['SEMI', self.input[self.pos]])
                elif self.input[self.pos] == ',':
                    self.token.append(['COMMA', self.input[self.pos]])
            elif self.input[self.pos].isalpha():
                self.tokenize_ID()
            elif self.input[self.pos] == ' " ':
                self.tokenize_STRING()
            elif self.input[self.pos] == ' ':
                self.tokenize_DELETE_space()
            elif self.input[self.pos] == '/*':
                self.tokenize_DELETE_comments()

    def tokenize_INTEGERS(self):
        while self.pos < len(self.input):
                token = self.input[self.pos]
                self.pos += 1
                while self.pos < len(self.input) and self.input[self.pos] in self.digits:
                    token += self.input[self.pos]
                    self.pos += 1
                self.tokens.append(('INTEGER', token))
            

    def tokenize_ID(self):
        while self.pos < len(self.input):
                token = self.input[self.pos]
                self.pos += 1
                while self.pos < len(self.input) and (self.input[self.pos].isalpha() or self.input[self.pos].isdigit()):
                    token += self.input[self.pos]
                    self.pos += 1
                self.tokens.append(('IDENTIFIER', token))

    def tokenize_STRING(self):
        while self.pos < len(self.input):
                token = self.input[self.pos]
                self.pos += 1
                while self.pos < len(self.input) and self.input[self.pos] != '"':
                    token += self.input[self.pos]
                    self.pos += 1
                token += self.input[self.pos]
                self.tokens.append(('STRING', token))

    def tokenize_DELETE_space(self):
        while self.pos < len(self.input):
                token = self.input[self.pos]
                self.pos += 1
                while self.pos < len(self.input) and self.input[self.pos] != ' ':
                    token += self.input[self.pos]
                    self.pos += 1
                self.tokens.append(('DELETE', token))

    def tokenize_DELETE_comments(self):
        while self.pos < len(self.input):
                token = self.input[self.pos]
                self.pos += 1
                while self.pos < len(self.input) and self.input[self.pos] != '*/':
                    token += self.input[self.pos]
                    self.pos += 1
                token += self.input[self.pos]
                self.tokens.append(('DELETE', token))