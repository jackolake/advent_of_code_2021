import pandas
import numpy
import queue

if __name__ == '__main__':
    heightmap = None
    # input
    with open('inputs/day_9.txt', 'r') as txt:
        # Pad left and right with '9'
        heightmap = pandas.DataFrame([[9] + [int(c) for c in line.strip()] + [9] for line in txt.readlines()])
    pad = pandas.DataFrame([[9] * heightmap.shape[1]])
    heightmap = pandas.concat([pad, heightmap, pad], ignore_index=True)  # Pad top and bottom with '9'

    # Get Basins (value less than: up, down, left, right)
    basin_mask = (heightmap.diff(1, axis=0) < 0) & (heightmap.diff(-1, axis=0) < 0) &\
                 (heightmap.diff(1, axis=1) < 0) & (heightmap.diff(-1, axis=1) < 0)
    basins_coordinates = [(x, y) for x, y in zip(*numpy.nonzero(basin_mask.values))]  # (col, row)

    # Part 1: sum of (basin value + 1)
    print(sum([heightmap.iloc[coord] + 1 for coord in basins_coordinates]))  # 535

    # Part 2: Flood-fill from basin
    clusters = []
    explore_queue = queue.Queue()
    for b in basins_coordinates:
        cluster = set([b])  # cluster seed
        explore_queue.put(b)
        while not explore_queue.empty():
            coord = explore_queue.get()
            for test_coord in [(coord[0] + 1, coord[1]), (coord[0], coord[1] + 1),
                               (coord[0] - 1, coord[1]), (coord[0], coord[1] - 1)]:  # Up, Down, Left, Right
                if heightmap.iloc[test_coord] != 9\
                        and heightmap.iloc[test_coord] > heightmap.iloc[coord]\
                        and test_coord not in cluster:  # Non-visited higher ground
                    explore_queue.put(test_coord)
                    cluster.add(test_coord)
        clusters.append(cluster)
    max_three_cluster_sizes = sorted([len(cluster) for cluster in clusters])[-3:]
    print(max_three_cluster_sizes[0] * max_three_cluster_sizes[1] * max_three_cluster_sizes[2])  # 1122700
