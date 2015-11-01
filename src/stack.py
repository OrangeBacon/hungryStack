# ----------
# hungryStack interpreter
# runs the provided file in the command line
# usage: py stack.py -h (help)
# usage: py stack.py -i file.hst (run)
# ----------
# ----------
# import modules
# ----------
import sys
from compilerHelp import *
from methods import *
from main import *

# ----------
# main
# ----------
if "-h" in sys.argv:
    Help(sys.argv)
elif "-i" not in sys.argv:
    error(string(sys.argv),len(string(sys.argv)),"Requires input file to run or the '-h' argument to display help")
elif len(sys.argv) < 3:
    error(string(sys.argv),len(string(sys.argv)),"File input required for '-i' argument")
elif len(sys.argv) > 3:
    error(string(sys.argv),len(sys.argv[0] + " " + sys.argv[1] + " " + sys.argv[2] + "  "),"Too many arguments provided")
else:
    try:
        with open(sys.argv[2]) as prog:
            run(sys.argv[2])
    except IOError:
        error(string(sys.argv),len(string(sys.argv))-len(sys.argv[2]),"File not found or incorrect permissions (IOError)")
