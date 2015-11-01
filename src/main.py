from commands import *
from methods import *
def run(file):
    #get prog
    with open(file) as prog:
        data = prog.read()

    #init vars
    part = 1
    line = ""
    qu = 0
    args = []
    exe = []
    stack = []

    #split prog into the commands and the arguments
    for x in range(0,len(data)):
        if data[x] == "\"":
            if qu == 0:
                qu = 1
            else:
                qu = 0
        else:
            if (data[x] == " " or data[x] == "\n" or data[x] == ";") and qu != 1:
                if part == 1:
                    if line != "":
                        args.append(line)
                elif part == 2:
                    if line != "":
                        exe.append(line)
                line = ""
            else:
                line = line + data[x]
        if data[x] == ";":
            part = 2
    if part == 1:
        args.append(line)
    elif part == 2:
        exe.append(line)
    #get dicts
    com = commands()
    cod = code()
    
    #run the commands
    arg = 0
    prog = 0
    while prog < len(exe):
        exist = com.get(exe[prog])
        if not exist:
            error("line " + str(prog) + " " + exe[prog] ,1 + len("line " + str(prog) + " "),"command " + exe[prog] + " is not identified")
        else:
            exec(cod.get(exe[prog]))
            arg = int(arg) + int(com.get(exe[prog]))
            prog = int(prog) + 1
        

















