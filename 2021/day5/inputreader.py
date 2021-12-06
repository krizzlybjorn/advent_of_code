from enum import Enum, auto

# I realize I ought to expand and reuse code, but my intention was to try different languages.

class ReadType(Enum):
    PROBLEMA = auto()

class InputReader():
    def __init__(self, file, target):
        self.input = open(file, "r")
        self.output = self.parse(target)

    def parse(self, target):
        if target == ReadType.PROBLEMA:
            retList = []
            for line in self.input:
                preSplit = line.strip().split(" -> ")
                first = preSplit[0].split(",")
                secon = preSplit[1].split(",")
                points = [[int(first[0]), int(first[1])] , [int(secon[0]), int(secon[1])]]
                retList.append(points)
            return retList