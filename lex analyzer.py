class lex:
    def __init__(self, input):
        self.input = input
        self.pos = -1
        self.current_char = None
        self.operator_symbol = ['+', '-', '*', '/', '(', ')', '{', '}', '[', ']', ';', ',', '<', '>', '=', '!', '&', '|']
        self.digits = '0123456789'
        self.punctuation = ['(', ')', ';', ',']
        self.tokens = []



    def advance(self):
        self.pos += 1
        self.current_char = self.input[self.pos] if self.pos < len(self.input) else None
            
    def lex(self):
        while self.pos < len(self.input):
            if self.input[self.pos] in self.digits:
                self.tokenize_INTEGERS()
            elif self.input[self.pos] in self.ops:
                if self.input[self.pos] == '+':
                    self.token.append(['PLUS',self.input[self.pos]])
                elif self.input[self.pos] == '-':
                    self.token.append(['SUB', self.input[self.pos]])
                elif self.input[self.pos] == '*':
                    self.token.append(['MULT', self.input[self.pos]])
                elif self.input[self.pos] == '/':
                    self.token.append(['DIV', self.input[self.pos]])
                elif self.input[self.pos] == '&':
                    self.token.append(['AND', self.input[self.pos]])
                elif self.input[self.pos] == '|':
                    self.token.append(['OR', self.input[self.pos]])
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
                


    def tokenize_INTEGERS(self):
        while self.pos < len(self.input):
            if self.input[self.pos] in self.digits:
                token = self.input[self.pos]
                self.pos += 1
                while self.pos < len(self.input) and self.input[self.pos] in self.digits:
                    token += self.input[self.pos]
                    self.pos += 1
                self.tokens.append(('INTEGER', token))
            else:
                self.pos += 1

    def tokenize_ID(self):
        while self.pos < len(self.input):
            if self.input[self.pos].isalpha():
                token = self.input[self.pos]
                self.pos += 1
                while self.pos < len(self.input) and (self.input[self.pos].isalpha() or self.input[self.pos].isdigit()):
                    token += self.input[self.pos]
                    self.pos += 1
                self.tokens.append(('ID', token))
            else:
                self.pos += 1
                
            
        