class lex:
    def __init__(self, input):
        self.input = input
        self.pos = 0
        self.tokens = []
        self.digits = '0123456789'
        self.ops = ['+', '-', '*', '/', '(', ')', '{', '}', '[', ']', ';', ',', '<', '>', '=', '!', '&', '|']

    

    def lex(self):
        while self.pos < len(self.input):
            if self.input[self.pos] in self.digits:
                self.token.append('INT', self.input[self.pos])
                self.pos += 1
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
                
            
        