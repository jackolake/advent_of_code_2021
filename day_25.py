import pandas
import numpy


if __name__ == '__main__':
    # inputs
    with open('inputs/day_25.txt', 'r') as txt:
        grid = pandas.DataFrame([[c for c in line.strip()] for line in txt.readlines()])
    right_moves = [(row, col) for row, col in zip(*numpy.nonzero((grid == '>').values))]
    down_moves = [(row, col) for row, col in zip(*numpy.nonzero((grid == 'v').values))]
    height, width = grid.shape

    # process
    def run_move(right_moves, down_moves):
        new_right_moves = []
        new_down_moves = []
        has_moved = False
        for right_move in right_moves:
            test_coordinate = (right_move[0], (right_move[1] + 1) % width)
            if test_coordinate not in right_moves and test_coordinate not in down_moves:
                new_right_moves.append(test_coordinate)
                has_moved = True
            else:
                new_right_moves.append(right_move)
        for down_move in down_moves:
            test_coordinate = ((down_move[0] + 1) % height, down_move[1])
            if test_coordinate not in new_right_moves != '>' and test_coordinate not in down_moves:
                new_down_moves.append(test_coordinate)
                has_moved = True
            else:
                new_down_moves.append(down_move)
        return new_right_moves, new_down_moves, has_moved

    # Get result
    moved = True
    step = 0
    while moved:
        right_moves, down_moves, moved = run_move(right_moves, down_moves)
        step += 1

    print(step)  # 549
