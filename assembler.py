import re

class Instructions:
    PUSH,POP,SET,ADD,SUB,MUL,DIV,JUMP,HALT,PRINT,JUMPIFEQUAL,JUMPIFNOTEQUAL,JUMPIFGT,JUMPIFLT = range(1, 15)

class Assembler:
    def __init__(self):
        self.RE_PUSH = re.compile(r"push\W+(\d+)")
        self.RE_POP = re.compile(r"pop")

        self.out = []

    def assemble(self, code):
        for line in code.split("\n"):
            line = line.strip()

            # PUSH
            match = self.RE_PUSH.match(line)
            if(match):
                value = int(match.group(1))

                self.out.append(Instructions.PUSH)
                self.out.append(value)

            # POP
            match = self.RE_POP.match(line)
            if(match):
                self.out.append(Instructions.POP)

        return self.out

if __name__=="__main__":
    a = Assembler()
    print a.assemble("""
    push 5
    push 10
    pop
    """)
