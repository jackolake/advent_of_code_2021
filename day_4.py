import pandas
import numpy


if __name__ == '__main__':
    # input
    boards = []
    max_row, max_col = 5, 5
    with open('inputs/day_4.txt', 'r') as txt:
        row = 0
        for line in txt.readlines():
            if ',' in line:
                draws = [int(c) for c in line.strip().split(',')]  # First line
            elif len(line) > 1:
                if row == 0:
                    board_coordinates = {}
                nums = [int(c) for c in line.strip().replace('\n', '').split(' ') if c]  # one row
                for col in range(max_col):
                    board_coordinates[nums[col]] = (row, col)  # {number => (x, y) coordinates}
                row = (row + 1) % max_row
                if row == 0:
                    boards.append(board_coordinates)  # Got 5 rows, save the board

    def get_win_sequence():
        board_occupancy = [pandas.DataFrame(numpy.zeros((max_row, max_col))) for _ in boards]
        won_boards = []
        for draw in draws:
            for board_num, board in enumerate(boards):
                if not any([(b[0] == board_num) for b in won_boards]):  # process if not won yet
                    # Make a move in the board
                    draw_row, draw_col = board.get(draw, (None, None))
                    if (draw_row, draw_col) != (None, None):
                        board_occupancy[board_num][draw_row][draw_col] = 1
                        # Check winning condition (row or column)
                        if any([board_occupancy[board_num].iloc[i].sum() == max_row for i in range(max_row)]) \
                                or any([board_occupancy[board_num][j].sum() == max_col for j in range(max_col)]):
                            # get unmarked numbers
                            unmarked = sum([d for d, coord in board.items()
                                            if board_occupancy[board_num][coord[0]][coord[1]] == 0])
                            won_boards.append((board_num, draw*unmarked))
        return won_boards

    # Show results
    results = get_win_sequence()
    # Part 1
    print(results[0])  # 58838
    # Part 2
    print(results[-1])  # 6256
