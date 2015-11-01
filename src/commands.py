def commands():
    _com_ = {}
    _com_["out"] = 1
    _com_["inp"] = 1
    _com_["add"] = 2
    _com_["sub"] = 2
    _com_["mul"] = 2
    _com_["div"] = 2
    return _com_

def code():
    _code_ = {}
    _code_["out"] = "inp = args[arg]\nif inp[0] != \"`\":\n    print(inp)\nelse:\n    inp = inp[1:]\n    print(stack[int(inp)])"
    _code_["inp"] = "stack.append(input(args[int(arg)]))"
    _code_["add"] = "stack.append(int(stack[int(args[arg][1:])]) + int(stack[int(args[arg+1][1:])]))"
    _code_["sub"] = "stack.append(int(stack[int(args[arg][1:])]) - int(stack[int(args[arg+1][1:])]))"
    _code_["mul"] = "stack.append(int(stack[int(args[arg][1:])]) * int(stack[int(args[arg+1][1:])]))"
    _code_["div"] = "stack.append(int(stack[int(args[arg][1:])]) / int(stack[int(args[arg+1][1:])]))"
    return _code_
