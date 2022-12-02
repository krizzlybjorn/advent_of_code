#ROCK  A X 1
#PAPER B Y 2
#SCISS C Z 3

#WIN 6
# A Y
# B Z
# C X

#DRAW 3
# A X
# B Y
# C Z

#LOOSE 0
# all other

#Not that many
#A X 4
#A Y 8
#A Z 3
#B X 1
#B Y 5
#B Z 9
#C X 7
#C Y 2
#C Z 6

score = 0

input_data = open("../input/input", "r")

for line in input_data:
    line = line.replace('\n', '')
    match line:
        case "A X":
            score += 4
        case "A Y":
            score += 8
        case "A Z":
            score += 3
        case "B X":
            score += 1
        case "B Y":
            score += 5
        case "B Z":
            score += 9
        case "C X":
            score += 7
        case "C Y":
            score += 2
        case "C Z":
            score += 6

print(score)


#Still not that many
#A X 0 + 3
#A Y 3 + 1
#A Z 6 + 2
#B X 0 + 1
#B Y 3 + 2
#B Z 6 + 3
#C X 0 + 2
#C Y 3 + 3
#C Z 6 + 1

score = 0

input_data = open("../input/input", "r")

for line in input_data:
    line = line.replace('\n', '')
    match line:
        case "A X":
            score += 3
        case "A Y":
            score += 4
        case "A Z":
            score += 8
        case "B X":
            score += 1
        case "B Y":
            score += 5
        case "B Z":
            score += 9
        case "C X":
            score += 2
        case "C Y":
            score += 6
        case "C Z":
            score += 7

print(score)
