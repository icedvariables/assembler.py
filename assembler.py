import re

class Assembler:
    def __init__(self):
        self.instructions = {"PUSH":0x1,"POP":0x2,"SET":0x3,"ADD":0x4,"SUB":0x5,"MUL":0x6,"DIV":0x7,"JUMP":0x8,"HALT":0x9,
                             "PRINT":0xA,"JUMPIFEQUAL":0xB,"JUMPIFNOTEQUAL":0xC,"JUMPIFGT":0xD,"JUMPIFLT":0xE}

        self.out = []

    def assemble(self, code):
        for line in code.split("\n"):
            line = line.strip().replace(" " * 2, " ").upper()
            split = line.split(" ")

            if not(line):
                continue

            if(len(split) > 0):
                if(split[0] in self.instructions.keys()):
                    instruction = self.instructions[split[0]]

                    self.out.append(instruction) # Add instruction
                    self.out.extend(split[1:])   # Add arguments
                else:
                    print "Unknown instruction:", split[0]



        return self.out

if __name__=="__main__":
    a = Assembler()
    print a.assemble("""
    push 5
    push 10
    pop
    """)
