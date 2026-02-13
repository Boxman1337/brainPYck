 

class Interpreter:
    def __init__(self, program: str, size: int):
        assert size >= 1000, "Tape size too small!"
        self.program = program
        self.size = size
        self.tape = [0] * size
        self.dataIdx = 0
        self.instructionIdx = 0

    # TODO: Rework control flow
    def getInstruction(self):
        match self.program[self.instructionIdx]:
            case '+':
                self.increment()
            case '-':
                self.decrement()
            case '.':
                self.output()
            case ',':
                self.input()
            case '>':
                self.moveRight()
            case '<':
                self.moveLeft()
            case '[':
                self.jumpEqZ()
            case ']':
                self.jumpNeZ()
            case _:
                self.instructionIdx += 1
            
    def run(self):
        while (self.instructionIdx < len(self.program)):
            self.getInstruction()

    def input(self):
        # TODO: Add character input
        pass

    def output(self):
        print(chr(self.tape[self.dataIdx]), end="")
        self.instructionIdx += 1
    
    # TODO: Add bound checking, wrap-around
    def moveLeft(self):
        self.dataIdx -= 1
        self.instructionIdx += 1

    # TODO: Add bound checking, wrap-around
    def moveRight(self):
        self.dataIdx += 1
        self.instructionIdx += 1

    def increment(self):
        curr = self.tape[self.dataIdx]
        self.tape[self.dataIdx] = (curr + 1) % 256
        self.instructionIdx += 1

    def decrement(self):
        curr = self.tape[self.dataIdx]
        self.tape[self.dataIdx] = (curr - 1) % 256
        self.instructionIdx += 1

    # TODO: Add jump table, currently O(n^2)
    def jumpEqZ(self):
        if (self.tape[self.dataIdx] != 0):
            self.instructionIdx += 1
            return 

        idx = self.instructionIdx
        counter = 0
        while (True):
            idx += 1
            if (self.program[idx] == '['):
                counter += 1

            if (self.program[idx] == ']'):
                if (counter == 0):
                    self.instructionIdx = idx + 1
                    break
                else:
                    counter -= 1

    # TODO: Add jump table, currently O(n^2)
    def jumpNeZ(self):
        if (self.tape[self.dataIdx] == 0):
            self.instructionIdx += 1
            return

        idx = self.instructionIdx
        counter = 0
        while (True):
            idx -= 1
            if (self.program[idx] == ']'):
                counter += 1

            if (self.program[idx] == '['):
                if (counter == 0):
                    self.instructionIdx = idx + 1
                    break
                else:
                    counter -= 1


def main():
    program = "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++.>+.+++++++..+++.<<++.>+++++++++++++++.>.+++.------.--------."
    i = Interpreter(program, 1000)
    i.run()

if __name__ == "__main__":
    main()
