import input

def solve_A():
    f = open("input_day_01", "r")
    ret_Val = -1
    last_val = 0
    for element in f:
        if int(element.strip()) > last_val:
            ret_Val += 1
        last_val = int(element.strip())
    return ret_Val

# Denne e stygg men funke, skriv om når eg føle for.
def solve_B():
    f = open("input_day_01", "r")
    list_data = []
    for line in f:
        list_data.append(int(line.strip()))
    list_slide = []
    for i in range(len(list_data)):
        try:
            list_slide.append(list_data[i]+list_data[i+1]+list_data[i+2])
        except:
            continue
    ret_Val = 0
    for i in range(len(list_slide)):
        if i == 0:
            continue
        if list_slide[i] > list_slide[i-1]:
            ret_Val += 1
    return ret_Val

def new_solve_A():
    parsed = input.Parser("input_day_01", input.TargetType.INT)
    inputfile = parsed.output
    ret_val = 0
    for i in range(len(inputfile)-1):
        if inputfile[i] < inputfile[i+1]:
            ret_val += 1
    return ret_val

# mye bedre - færre loops, ingen unødvendig except continue for å håndtere out of bounds, lettleselig
def new_solve_B():
    parsed = input.Parser("input_day_01", input.TargetType.INT).output
    ret_val = 0
    for i in range(len(parsed)-2):
        if sum(parsed[i:i+3]) < sum(parsed[i+1:i+4]):
            ret_val += 1
    return ret_val