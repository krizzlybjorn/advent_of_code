import input_reader

def solve_A():
    parsed = input_reader.InputReader("../input/input_day_01", input_reader.ParseInputAs.INT)
    inputfile = parsed.output
    ret_val = 0
    for i in range(len(inputfile)-1):
        if inputfile[i] < inputfile[i+1]:
            ret_val += 1
    return ret_val

def solve_B():
    parsed = input_reader.InputReader("../input/input_day_01", input_reader.ParseInputAs.INT).output
    ret_val = 0
    for i in range(len(parsed)-2):
        if sum(parsed[i:i+3]) < sum(parsed[i+1:i+4]):
            ret_val += 1
    return ret_val