import pandas
import numpy


if __name__ == '__main__':
    # input
    vent_lines = []
    max_row, max_col = 1, 1
    with open('inputs/day_5.txt', 'r') as txt:
        for line in txt.readlines():
            origin, dest = line.strip().split('->')
            x1, y1 = origin.split(',')
            x2, y2 = dest.split(',')
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            vent_lines.append(((x1, y1), (x2, y2)))
            max_row = max([max_row, y1+1, y2+1])
            max_col = max([max_col, x1+1, x2+1])


    def generate_grid(skip_diagonal=True):
        grid = pandas.DataFrame(numpy.zeros((max_row, max_col)))
        for origin, dest in vent_lines:
            (x1, y1), (x2, y2) = origin, dest
            if x1 == x2:
                for i in range(min(y1, y2), max(y1, y2) + 1):
                    grid[x1][i] += 1
            elif y1 == y2:
                for j in range(min(x1, x2), max(x1, x2) + 1):
                    grid[j][y1] += 1
            elif not skip_diagonal:
                x_increment = 1 if x2 > x1 else -1
                y_increment = 1 if y2 > y1 else -1
                for i in range(abs(x2 - x1)+1):  # 698,289 -> 893,94
                    grid[x1 + i * x_increment][y1 + i * y_increment] += 1
        return grid

    # Part 1
    grid = generate_grid(skip_diagonal=True)
    print(sum([1 for i in range(max_row) for j in range(max_col) if grid[j][i] > 1]))  # 5835

    # Part 2
    grid = generate_grid(skip_diagonal=False)
    print(sum([1 for i in range(max_row) for j in range(max_col) if grid[j][i] > 1]))  # 17013
