import pandas
import queue
from math import nan, inf
import numpy


def run_simulation(grid, iterations):  # iterations = -1 means stop only when everything flashes
    expected_full_slots = (grid.shape[0] - 2) * (grid.shape[1] - 2)
    # Run simulation
    flashes = []
    iteration_count = 0
    while True:
        # Increment
        new_grid = grid + 1
        # Handle flash
        new_flash = queue.Queue()
        flashed = set()
        # Find first flash
        flash_coordinates = [(x, y) for x, y in zip(*numpy.nonzero((new_grid > 9).values))]  # (col, row)
        for flash_coordinate in flash_coordinates:
            new_flash.put(flash_coordinate)
        while not new_flash.empty():
            # Keep processing the flashes
            flash_coordinate = new_flash.get()
            if flash_coordinate not in flashed:
                new_grid.iloc[flash_coordinate] = 0
                for y_mod, x_mod in ([(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]):
                    test_coordinate = (flash_coordinate[0] + y_mod, flash_coordinate[1] + x_mod)
                    if (test_coordinate[0] not in (0, grid.shape[0] - 1)) \
                            and (test_coordinate[1] not in (0, grid.shape[1] - 1)):  # not out of bound
                        if test_coordinate not in flashed:
                            new_grid.iloc[test_coordinate] += 1  # Flash effect on neighbour
                            if new_grid.iloc[test_coordinate] > 9:
                                new_flash.put(test_coordinate)
                flashed.add(flash_coordinate)
        grid = new_grid
        flashes.append(flashed)
        iteration_count += 1
        if (iterations == -1 and len(flashed) == expected_full_slots) \
                or (iterations != -1 and iteration_count >= iterations):
            break
    return flashes


if __name__ == '__main__':
    # input
    with open('inputs/day_11.txt', 'r') as txt:
        grid = pandas.DataFrame([[nan] + [int(c) for c in line.strip()] + [nan] for line in txt.readlines()])
    # Add padding
    grid = pandas.concat([pandas.DataFrame([[nan] * grid.shape[1]]),
                          grid,
                          pandas.DataFrame([[nan] * grid.shape[1]])], ignore_index=True)

    # Part 1
    flashes = run_simulation(grid, iterations=100)
    print(sum([len(flash) for flash in flashes]))

    # Part 2
    flashes = run_simulation(grid, iterations=-1)
    print(len(flashes))
