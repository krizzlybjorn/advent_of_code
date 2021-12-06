from enum import Enum, auto
import pandas as pd


class InputReaderEnum(Enum):
    DAY4A = auto()
    DAY4B = auto()


class InputReader:
    def __init__(self, file, target: InputReaderEnum):
        self.input = open(file, "r")
        self.output = self.parse(target)
        if target == InputReaderEnum.DAY4A:
            self.output_alt = self.output[0]
            self.output = self.fix_output_for_A(self.output[1:])
    
    def parse(self, target):
        if target == InputReaderEnum.DAY4A:
            retList = []
            doOnce = True
            for line in self.input:
                if doOnce:
                    retList.append([int(x) for x in line.strip().split(",")])
                    doOnce = False
                elif line == "\n":
                    retList.append('')
                else:
                    retList.append([int(x) for x in line.strip().split()])
            return retList
        elif target == InputReaderEnum.DAY4B:
            return NotImplementedError()

    def reverselist(self, lst):
        new_list = lst[::-1]
        return new_list

    def fix_output_for_A(self, lst):
        tmp_lst = [ele for ele in lst if type(ele) == list or ele.strip()]
        n = len(tmp_lst[0])
        return [tmp_lst[i * n:(i + 1) * n] for i in range((len(tmp_lst) + n - 1) // n )] 

class Board:
    def __init__(self, listOfList):
        self.max_index = len(listOfList)
        self.value_board = pd.DataFrame(listOfList, columns=range(self.max_index))
        self.bool_board = pd.DataFrame(index=range(self.max_index), columns=range(self.max_index))
        for i in range(self.max_index):
            self.bool_board[i] = False
        self.has_bingo = False
        self.won_on_turn = 0
        self.bingo_score = 0
        self._turn_counter = 0

    def __str__(self):
        return self.value_board.to_string()

    def display_bool_board(self):
        print(self.bool_board.to_string())

    def next_value(self, value):
        self._turn_counter += 1
        for i in range(self.max_index):
            for j in range(self.max_index):
                if self.value_board.iloc[j,i] == value:
                    self.bool_board.iloc[j,i] = True
        if not self.has_bingo:
            self.check_bingo_all(value)

    def check_bingo_all(self, value):
        if self.check_bingo_diag_down() or self.check_bingo_diag_up() or self.check_bingo_col() or self.check_bingo_row():
            self.has_bingo = True
            self.won_on_turn = self._turn_counter
            self.bingo_score = self.get_score(value)

    def check_bingo_diag_precheck(self):
        # only boards with halfway points can have diagonal bingo
        # while probably insignificant for so small boards, should speed up checking in larger boards
        if (self.max_index-1 % 2) == 0:
            if self.bool_board.iloc[(self.max_index-1)/2, (self.max_index-1)/2] == True:
                return True
        return False

    def check_bingo_diag_down(self):
        if self.check_bingo_diag_precheck() == False:
            return False
        for i in range(self.max_index):
            if self.bool_board.iloc[i,i] == True:
                continue
            else:
                return False
        return True
    
    def check_bingo_diag_up(self):
        for i in range(self.max_index):
            if self.bool_board.iloc[self.max_index -1 -i, i] == True:
                continue
            else:
                return False
        return True

    def check_col_on_board(self, board):
        for i in range(self.max_index):
            temp_bool = True
            for j in range(self.max_index):
                if board.iloc[j,i] == False:
                    temp_bool = False
                    break
            if temp_bool:
                return True
        return False

    def check_bingo_col(self):
        return self.check_col_on_board(self.bool_board)

    def check_bingo_row(self):
        return self.check_col_on_board(self.bool_board.transpose())

    def get_score(self, value):
        score = 0
        for i in range(self.max_index):
            for j in range(self.max_index):
                if self.bool_board.iloc[j,i] == False:
                    score += self.value_board.iloc[j,i]
        return score * value

class BingoGame:
    def __init__(self, steps, boards):
        self.numbers = steps
        self.boards = [Board(x) for x in boards]
        self.winner = False
        self.win_number = 0
        self.winnerscore = 0

    def play_untill_winner(self):
        for value in self.numbers:
            for board in self.boards:
                board.next_value(value)
                if board.has_bingo:
                    self.winner = True
            if self.winner:
                self.win_number = value
                #self.debug_print_winner()
                return self.get_scores()

    def play_untill_end(self):
        for value in self.numbers:
            for board in self.boards:
                board.next_value(value)

    def get_score_of_last_winner(self):
        self.play_untill_end()
        winning_turn = 0
        for board in self.boards:
            if board.won_on_turn > winning_turn:
                winning_turn = board.won_on_turn
        return [(element.bingo_score) for element in self.boards if element.won_on_turn == winning_turn]


    def get_scores(self):
        if self.winner == False:
            return
        self.winnerscore = [x.bingo_score for x in self.boards if x.has_bingo]
        return self.winnerscore

    def debug_print_winner(self):
        for board in self.boards:
            if board.has_bingo:
                print(board)
                print(board.bool_board)


def solve_A():
    print("Part A: ")
    data = InputReader("input_day_04", InputReaderEnum.DAY4A)
    game = BingoGame(data.output_alt, data.output)
    print(game.play_untill_winner())

def solve_B():
    print("Part B: ")
    data = InputReader("input_day_04", InputReaderEnum.DAY4A)
    game = BingoGame(data.output_alt, data.output)
    print(game.get_score_of_last_winner())

if __name__ == "__main__":
    solve_A()
    solve_B()