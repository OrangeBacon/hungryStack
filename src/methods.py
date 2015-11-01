import sys
def string(List):
    out = ""
    for x in range(0,len(List)):
        out = out + List[x] + " "
    return(out)

def error(line,char,message):
    print("ERROR")
    print(line)
    space = ""
    for x in range(0,char-1):
        space = space + " "
    print(space + "^")
    print(message)
    sys.exit
