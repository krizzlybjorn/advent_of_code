from enum import Enum, auto

class TargetType(Enum):
    LIST = auto()
    INT = auto()
    STR = auto()
    SPLIT = auto()

class Parser:
    def __init__(self, file, target):
        self.input = open(file, "r")
        self.output = self.parse(target)

    def parse(self, target):
        match target:
            case TargetType.LIST:
                return [x for x in self.input]
            case TargetType.INT:
                return [int(x) for x in self.input]
            case TargetType.STR:
                return [str(x) for x in self.input]
            case TargetType.SPLIT:
                return [x.split() for x in self.input]

