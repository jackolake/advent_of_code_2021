import pandas


def new_max_size(axis, max_size):
    return max_size - abs(max_size - axis)


def flip(axis, current, max_size):  # 1D flip
    if current < axis:
        if axis >= max_size / 2:  # unchanged
            return current
        else:  # new max_size = (max_size - axis - 1), old distance from axis = new distance from new max_size
            return (max_size - axis - 1) - (axis - current)
    elif current > axis:
        if axis >= max_size / 2:
            return axis - (current - axis)  # new max_size = axis, old distance from axis = new distance from axis
        else:  # new max_size = (max_size - axis - 1), old distance from axis = new distance from max_size
            return (max_size - axis - 1) - (current - axis)


def run_flips(input_max_row, input_max_col, input_dots, input_flips):
    ret_max_row, ret_max_col, ret_dots = input_max_row, input_max_col, input_dots
    for flip_xy, flip_axis in input_flips:
        if flip_xy == 'y':
            ret_dots = [(flip(flip_axis, d[0], ret_max_row), d[1]) for d in ret_dots]
            ret_max_row = new_max_size(flip_axis, ret_max_row)
        else:
            ret_dots = [(d[0], flip(flip_axis, d[1], ret_max_col)) for d in ret_dots]
            ret_max_col = new_max_size(flip_axis, ret_max_col)
    return ret_max_row, ret_max_col, ret_dots


if __name__ == '__main__':
    # input
    dots = []  # (row, col)
    flips = []  # ('x' or 'y', axis)
    with open('inputs/day_13.txt', 'r') as txt:
        for line in txt.readlines():
            if ',' in line:
                col, row = line.strip().split(',')
                dots.append((int(row), int(col)))
            elif '=' in line:
                xy, num = line.strip().split(' ')[-1].split('=')
                flips.append((xy, int(num)))
    max_row, max_col = max([d[0] for d in dots]) + 1, max([d[1] for d in dots]) + 1

    # Part1
    _, _, part1_dots = run_flips(max_row, max_col, dots, flips[:1])
    print(len(set(part1_dots)))  # 669

    # Part 2
    r, c, part2_dots = run_flips(max_row, max_col, dots, flips)
    # Draw diagram
    grid = pandas.DataFrame([[' '] * c] * r)
    for coord in part2_dots:
        grid.iloc[coord] = '#'
    for row in grid.values:
        print(''.join(row))  # UEFZCUCJ
