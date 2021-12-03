from enum import Enum, auto
from pathlib import Path

class ParseInputAs(Enum):
    LIST = auto()
    INT = auto()
    STR = auto()
    SPLIT = auto()

class InputReader:
    def __init__(self, file, target):
        self.input = open(Path(__file__).parent / file, "r")
        self.output = self.parse(target)
    
    def parse(self, target):
        if target == ParseInputAs.LIST:
            return [x for x in self.input]
        elif target == ParseInputAs.INT:
            return [int(x) for x in self.input]
        elif target == ParseInputAs.STR:
            return [str(x) for x in self.input]
        elif target == ParseInputAs.SPLIT:
            return [x.split() for x in self.input]


# Python 3.10 not in pacman, can't be bothered to fix. Use this when match case is back
#    def parse(self, target):
#        match target:
#            case TargetType.LIST:
#                return [x for x in self.input]
#            case TargetType.INT:
#                return [int(x) for x in self.input]
#            case TargetType.STR:
#                return [str(x) for x in self.input]
#            case TargetType.SPLIT:
#                return [x.split() for x in self.input]