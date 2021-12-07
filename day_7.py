if __name__ == '__main__':
    crab_positions = []
    # input
    with open('inputs/day_7.txt', 'r') as txt:
        for line in txt.readlines():
            crab_positions = [int(num) for num in line.strip().split(',')]

    max_pos = max(crab_positions)
    # Part 1
    part1 = dict([(alignment, sum([int(abs(pos-alignment)) for pos in crab_positions]))
                 for alignment in range(max_pos + 1)])  # {alignment: fuel}
    print(min(part1.values()))  # min fuel: 356992

    # Part 2
    fuel_map = [0]  # fuel_map[step] = fuel
    for i in range(1, max_pos + 1):
        fuel_map.append(fuel_map[i - 1] + i)
    part2 = dict([(alignment, sum([fuel_map[int(abs(pos-alignment))] for pos in crab_positions]))
                 for alignment in range(max_pos + 1)])  # {alignment: fuel}
    print(min(part2.values()))  # min fuel: 101268110
