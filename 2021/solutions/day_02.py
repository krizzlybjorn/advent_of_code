import input_reader

def solve_A():
    data = input_reader.InputReader("../input/input_day_02", input_reader.ParseInputAs.SPLIT).output
    hor_pos = 0
    dep_pos = 0
    for element in data:
        if element[0] == "forward":
            hor_pos += int(element[1])
        elif element[0] == "down":
            dep_pos += int(element[1])
        elif element[0] == "up":
            dep_pos -= int(element[1])
    return hor_pos*dep_pos

def solve_B():
    data = input_reader.InputReader("../input/input_day_02", input_reader.ParseInputAs.SPLIT).output
    hor_pos = 0
    dep_pos = 0
    aim_val = 0
    for element in data:
        if element[0] == "forward":
            hor_pos += int(element[1])
            dep_pos += aim_val * int(element[1])
        elif element[0] == "down":
            aim_val += int(element[1])
        elif element[0] == "up":
            aim_val -= int(element[1])
    return hor_pos*dep_pos