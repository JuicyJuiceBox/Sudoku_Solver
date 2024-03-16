import random

class Sudoku:
    def __init__(self):
        self.columns = {
            'A': [(1, 'A'), (2, 'A'), (3, 'A'), (4, 'A'), (5, 'A'), (6, 'A'), (7, 'A'), (8, 'A'), (9, 'A')],
            'B': [(1, 'B'), (2, 'B'), (3, 'B'), (4, 'B'), (5, 'B'), (6, 'B'), (7, 'B'), (8, 'B'), (9, 'B')],
            'C': [(1, 'C'), (2, 'C'), (3, 'C'), (4, 'C'), (5, 'C'), (6, 'C'), (7, 'C'), (8, 'C'), (9, 'C')],
            'D': [(1, 'D'), (2, 'D'), (3, 'D'), (4, 'D'), (5, 'D'), (6, 'D'), (7, 'D'), (8, 'D'), (9, 'D')],
            'E': [(1, 'E'), (2, 'E'), (3, 'E'), (4, 'E'), (5, 'E'), (6, 'E'), (7, 'E'), (8, 'E'), (9, 'E')],
            'F': [(1, 'F'), (2, 'F'), (3, 'F'), (4, 'F'), (5, 'F'), (6, 'F'), (7, 'F'), (8, 'F'), (9, 'F')],
            'G': [(1, 'G'), (2, 'G'), (3, 'G'), (4, 'G'), (5, 'G'), (6, 'G'), (7, 'G'), (8, 'G'), (9, 'G')],
            'H': [(1, 'H'), (2, 'H'), (3, 'H'), (4, 'H'), (5, 'H'), (6, 'H'), (7, 'H'), (8, 'H'), (9, 'H')],
            'I': [(1, 'I'), (2, 'I'), (3, 'I'), (4, 'I'), (5, 'I'), (6, 'I'), (7, 'I'), (8, 'I'), (9, 'I')]
        }
        self.rows = {
            1: [(1, 'A'), (1, 'B'), (1, 'C'), (1, 'D'), (1, 'E'), (1, 'F'), (1, 'G'), (1, 'H'), (1, 'I')],
            2: [(2, 'A'), (2, 'B'), (2, 'C'), (2, 'D'), (2, 'E'), (2, 'F'), (2, 'G'), (2, 'H'), (2, 'I')],
            3: [(3, 'A'), (3, 'B'), (3, 'C'), (3, 'D'), (3, 'E'), (3, 'F'), (3, 'G'), (3, 'H'), (3, 'I')],
            4: [(4, 'A'), (4, 'B'), (4, 'C'), (4, 'D'), (4, 'E'), (4, 'F'), (4, 'G'), (4, 'H'), (4, 'I')],
            5: [(5, 'A'), (5, 'B'), (5, 'C'), (5, 'D'), (5, 'E'), (5, 'F'), (5, 'G'), (5, 'H'), (5, 'I')],
            6: [(6, 'A'), (6, 'B'), (6, 'C'), (6, 'D'), (6, 'E'), (6, 'F'), (6, 'G'), (6, 'H'), (6, 'I')],
            7: [(7, 'A'), (7, 'B'), (7, 'C'), (7, 'D'), (7, 'E'), (7, 'F'), (7, 'G'), (7, 'H'), (7, 'I')],
            8: [(8, 'A'), (8, 'B'), (8, 'C'), (8, 'D'), (8, 'E'), (8, 'F'), (8, 'G'), (8, 'H'), (8, 'I')],
            9: [(9, 'A'), (9, 'B'), (9, 'C'), (9, 'D'), (9, 'E'), (9, 'F'), (9, 'G'), (9, 'H'), (9, 'I')]
        }
        self.grid_key = {

        }


        self.boxes = {
            'TL': [(1, 'A'), (1, 'B'), (1, 'C'),
                   (2, 'A'), (2, 'B'), (2, 'C'),
                   (3, 'A'), (3, 'B'), (3, 'C')],
            'TC': [(1, 'D'), (1, 'E'), (1, 'F'),
                   (2, 'D'), (2, 'E'), (2, 'F'),
                   (3, 'D'), (3, 'E'), (3, 'F')],
            'TR': [(1, 'G'), (1, 'H'), (1, 'I'),
                   (2, 'G'), (2, 'H'), (2, 'I'),
                   (3, 'G'), (3, 'H'), (3, 'I')],
            'CL': [(4, 'A'), (4, 'B'), (4, 'C'),
                   (5, 'A'), (5, 'B'), (5, 'C'),
                   (6, 'A'), (6, 'B'), (6, 'C')],
            'CC': [(4, 'D'), (4, 'E'), (4, 'F'),
                   (5, 'D'), (5, 'E'), (5, 'F'),
                   (6, 'D'), (6, 'E'), (6, 'F')],
            'CR': [(4, 'G'), (4, 'H'), (4, 'I'),
                   (5, 'G'), (5, 'H'), (5, 'I'),
                   (6, 'G'), (6, 'H'), (6, 'I')],
            'BL': [(7, 'A'), (7, 'B'), (7, 'C'),
                   (8, 'A'), (8, 'B'), (8, 'C'),
                   (9, 'A'), (9, 'B'), (9, 'C')],
            'BC': [(7, 'D'), (7, 'E'), (7, 'F'),
                   (8, 'D'), (8, 'E'), (8, 'F'),
                   (9, 'D'), (9, 'E'), (9, 'F')],
            'BR': [(7, 'G'), (7, 'H'), (7, 'I'),
                   (8, 'G'), (8, 'H'), (8, 'I'),
                   (9, 'G'), (9, 'H'), (9, 'I')]
        }

        self.marks = {

        }


        self.fill_stack = []


        self.unfilled = [k for k in self.grid_key]


    def hash_gen(self):
        row_x = self.rows.keys()
        col_y = self.columns.keys()
        cords = []
        for x in row_x:
            for y in col_y:
                cords.append((x, y))
        for cord in cords:
            self.grid_key[cord] = 0

    def mark_gen(self):
        col_keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        possible_vals = {1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True}
        for x in possible_vals:
            for y in col_keys:
                self.marks[(x, y)] = possible_vals


    def mark_scrub(self, x, y):
        scrub = self.grid_key[(x, y)]

        for r in self.rows[x]:
            if self.marks[r][scrub]:
                self.marks[r][scrub] = False
        for c in self.columns[y]:
            if self.marks[c][scrub]:
                self.marks[c][scrub] = False
        for box in self.boxes:
            if (x, y) in self.boxes[box]:
                for b in self.boxes[box]:
                    if self.marks[b][scrub]:
                        self.marks[b][scrub] = False
                break
            else:
                continue


    def backtrack(self):



    def fill_space(self):
        space = random.choice(self.unfilled)

        if any(i for i in self.marks[space].values()):
            choices = [i for i in self.marks[space] if self.marks[space][i]]
            choice = random.choice(choices)
            self.marks[space][choice] = False
            self.fill_stack.append(space)
            self.unfilled.remove(space)
            self.mark_scrub(*space)
        else:
            pass #insert call to backtrace here


    def print_grid(self):
        for r in range(1,10):
            line = [self.grid_key[xy] for xy in self.rows[r]]
            print(line)