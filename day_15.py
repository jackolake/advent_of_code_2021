from collections import defaultdict
import pandas
from math import inf
import heapq


def part2_modification(df):
    def _increment(t, iterations):
        ret = t
        for _ in range(iterations):
            ret = ret % 9 + 1
        return ret
    horizontal = pandas.DataFrame(pandas.concat([_increment(df, i) for i in range(0, 5)], axis=1).values)
    vertical = pandas.DataFrame(pandas.concat([_increment(horizontal, i) for i in range(0, 5)], axis=0).values)
    return vertical


if __name__ == '__main__':
    # inputs
    with open('inputs/day_15.txt', 'r') as txt:
        risk = pandas.DataFrame([[int(c) for c in line.strip()] for line in txt.readlines()])

    # Part2  (Remove this line for part 1)
    risk = part2_modification(risk)

    # init
    start, end = (0, 0), (risk.shape[0] - 1, risk.shape[1] - 1)
    risk_from_start = defaultdict(lambda: inf)  # {(row, col): risk_from_start}
    explorer_heap = [(0.0, start)]  # (risk_from_start, (row, col))
    heapq.heapify(explorer_heap)
    visited_nodes = set()

    # Explore
    while explorer_heap:
        explorer_risk, explorer_node = heapq.heappop(explorer_heap)  # Explore unvisited node closest to start
        if explorer_node not in visited_nodes:
            visited_nodes.add(explorer_node)  # Once visited, risk[explorer_node] cannot go smaller
            if explorer_node == end:  # early terminating condition
                break
            for mod_row, mod_col in [(1, 0), (0, 1), (-1, 0), (0, -1)]:  # Down, Right, Up, Left
                test_coord = (explorer_node[0] + mod_row, explorer_node[1] + mod_col)
                if 0 <= test_coord[0] < risk.shape[0] and 0 <= test_coord[1] < risk.shape[1]:  # Map bound
                    test_new_risk = explorer_risk + risk.iloc[test_coord]
                    if test_new_risk < risk_from_start[test_coord]:  # New smaller risk sum found, Save the result
                        risk_from_start[test_coord] = test_new_risk  # optionally: save prev[test_coord] = explorer_node
                    if test_coord not in visited_nodes:  # Mark unexplored neighbours for exploration later
                        heapq.heappush(explorer_heap, (risk_from_start[test_coord], test_coord))
    print(risk_from_start[end])  # part1: 824, part2: 3063
