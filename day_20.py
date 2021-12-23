from collections import defaultdict
import pandas
import numpy


def get_boundary(light_map):
    inf = int(10e6)
    min_row, max_row, min_col, max_col = inf, -inf, inf, -inf
    for row, col in light_map.keys():
        if row < min_row: min_row = row
        if row > max_row: max_row = row
        if col < min_col: min_col = col
        if col > max_col: max_col = col
    return (min_row, min_col), (max_row, max_col)


def run_enhancement(light_map, tape, default_light='0'):
    expand_margin = 1
    masks = [(row_mod, col_mod) for row_mod in range(-1, 2) for col_mod in range(-1, 2)]
    top_left, bottom_right = get_boundary(light_map)
    new_light_map = defaultdict(lambda: '0')
    for row in range(top_left[0] - expand_margin, bottom_right[0] + 1 + expand_margin):
        for col in range(top_left[1] - expand_margin, bottom_right[1] + 1 + expand_margin):
            binary_string = ''
            for mask in masks:
                test_row, test_col = row + mask[0], col + mask[1]
                if bottom_right[0] >= test_row >= top_left[0] and bottom_right[1] >= test_col >= top_left[1]:
                    binary_string += light_map[(row + mask[0], col + mask[1])]
                else:
                    binary_string += default_light
            if tape[int(binary_string, 2)] == '1':
                new_light_map[(row, col)] = '1'
    return new_light_map


if __name__ == '__main__':
    # inputs
    with open('inputs/day_20.txt', 'r') as txt:
        lines = [l.strip() for l in txt.readlines() if l.strip()]
    tape = ['1' if c == '#' else '0' for c in lines[0]]
    raw_pic = pandas.DataFrame([['1' if c == '#' else '0' for c in line] for line in lines[1:]])
    flicker = tape[0] != tape[-1]  # first bit = '#', last bit = '0' => flicker
    light_map = defaultdict(lambda: '0')
    for x, y in zip(*numpy.nonzero((raw_pic == '1').values)):
        light_map[(x, y)] = '1'

    # Run
    for i in range(50):  # Part 1 = 2 rounds, part2 = 50 rounds
        light_map = run_enhancement(light_map, tape, default_light='1' if flicker and (i % 2) == 1 else '0')
    print(len(light_map))  # Part1: 5464  Part2: 19228
