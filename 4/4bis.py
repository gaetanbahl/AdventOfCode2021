with open("input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]

class Grid():

    def __init__(self, lines):

        self.numbers = []
        self.n_checked = 0
        self.row_count = [0 for i in range(5)]
        self.col_count = [0 for i in range(5)]

        for l in lines:
            self.numbers.append([int(x) for x in l.split(" ") if x!=''])


    def mark_number(self, n):

        for r_i, row in enumerate(self.numbers):
            try:
                i = row.index(n)
                row[i] = -1
                self.row_count[r_i] += 1
                self.col_count[i] += 1
                self.n_checked += 1
                break
            except:
                pass
        return self.check_grid()

    
    def check_grid(self):
        return 5 in self.row_count or 5 in self.col_count


    def sum(self):
        return sum([sum(row) for row in self.numbers]) + self.n_checked

grid_lines = list(filter(lambda x: x!="", lines[1:]))

grids = [Grid(grid_lines[i:i+5]) for i in range(0,len(grid_lines),5)]

drawn = [int(x) for x in lines[0].split(",")]

points = []
for n in drawn:
    new_grids = []
    for g in grids:
        if g.mark_number(n):
            points.append(n*g.sum())
        else:
            new_grids.append(g)
    grids = new_grids

print(points)
