import input

def solve_A():
    data = input.Parser("input_day_02", input.TargetType.SPLIT).output
    hor_pos = 0
    dep_pos = 0
    for element in data:
        match element[0]:
            case "forward":
                hor_pos += int(element[1])
            case "down":
                dep_pos += int(element[1])
            case "up":
                dep_pos -= int(element[1])
    return hor_pos*dep_pos

def solve_B():
    data = input.Parser("input_day_02", input.TargetType.SPLIT).output
    hor_pos = 0
    dep_pos = 0
    aim_val = 0
    for element in data:
        match element[0]:
            case "forward":
                hor_pos += int(element[1])
                dep_pos += aim_val * int(element[1])
            case "down":
                aim_val += int(element[1])
            case "up":
                aim_val -= int(element[1])
    return hor_pos*dep_pos