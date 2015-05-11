import sys

class Assembler:
    def __init__(self):
        self.instructions = {"PUSH":0x1,"POP":0x2,"SET":0x3,"ADD":0x4,"SUB":0x5,"MUL":0x6,"DIV":0x7,"JUMP":0x8,"HALT":0x9,
                             "PRINT":0xA,"JUMPIFEQUAL":0xB,"JUMPIFNOTEQUAL":0xC,"JUMPIFGT":0xD,"JUMPIFLT":0xE}

        self.out = []

    def assemble(self, code):
        for lineNum, line in enumerate(code.split("\n")):
            line = line.strip().replace(" " * 2, " ").upper()
            split = line.split(" ")

            if not(line):
                continue

            if(len(split) > 0 and line[0] != ";"):
                if(split[0] in self.instructions.keys()):
                    instruction = self.instructions[split[0]]

                    print "Line", lineNum+1, "Instruction", instruction, "Arguments ", split[1:]

                    self.out.append(instruction) # Add instruction
                    self.out.extend(split[1:])   # Add arguments

                elif(line[0] == "#"): # preprocessor
                    command = split[0][1:].upper()

                    print "Preprocessor ", command

                    if(command == "OFFSET"):
                        amount = split[1]

                        self.out.extend([0] * int(amount))

                else:
                    print "Unknown instruction:", split[0]


        # convert to ints
        for i, val in enumerate(self.out):
            try:
                self.out[i] = int(val)
            except:
                continue

        return self.out

if __name__=="__main__":
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]

    try:
        with open(inputFile) as f:
            code = f.read()
    except IOError:
        print "Could not read file '" + inputFile + "'"
        sys.exit()

    a = Assembler()
    result = a.assemble(code)

    print "\n\n", result

    with open(outputFile, "wb") as f:
        f.write(bytearray(result))
