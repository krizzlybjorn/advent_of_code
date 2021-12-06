import inputreader
import pandas as pd

# data list
# data[0] line
# data[0][0] point
# data[0][0][0] single coordinate

# df[col, row]

class Board:
    def __init__(self):
        self.max = 1000 # chosen by guestimate, appears to be max
        self.df = pd.DataFrame(0, index=range(self.max), columns=range(self.max))
        self.processed_lines_tot = 0
        self.processed_lines_hor = 0
        self.processed_lines_ver = 0

    def process_line(self, line, isB):
        self.processed_lines_tot += 1

        # vertical line
        if line[0][0] == line[1][0]:
            self.processed_lines_ver += 1
            for row in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1]) + 1):
                self.df.iat[line[0][0], row] += 1
        # horizontal line
        elif line[0][1] == line[1][1]:
            self.processed_lines_hor += 1
            for col in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0]) + 1):
                self.df.iat[col, line[0][1]] += 1
        # diagonal line
        elif isB:
            if line[0][0] > line[1][0]:
                col_list = range(line[0][0], line[1][0] -1, -1)
            else:
                col_list = range(line[0][0], line[1][0] + 1)
            if line[0][1] > line[1][1]:
                row_list = range(line[0][1], line[1][1] -1, -1)
            else:
                row_list = range(line[0][1], line[1][1] + 1)
            for i in range(len(col_list)):
                    self.df.iat[col_list[i], row_list[i]] += 1

    def count_overlaps(self):
        retValue = 0
        for col in range(self.max):
            for row in range(self.max):
                if self.df.iloc[col,row] >= 2:
                    retValue += 1
        return retValue

def solve_A():
    data = inputreader.InputReader("input_day_05", inputreader.ReadType.PROBLEMA).output
    graph = Board()
    for line in data:
        graph.process_line(line, False)
    print(graph.count_overlaps())
#    print(graph.processed_lines_tot)
#    print(graph.processed_lines_hor)
#    print(graph.processed_lines_ver)

def solve_B():
    data = inputreader.InputReader("input_day_05", inputreader.ReadType.PROBLEMA).output
    graph = Board()
    for line in data:
        graph.process_line(line, True)
    print(graph.count_overlaps())

if __name__ == "__main__":
    # solve_A()
    solve_B()