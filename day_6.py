from collections import defaultdict

if __name__ == '__main__':
    fish_dict = defaultdict(int)  # {fish remaining cycle: number of fish}
    # input
    with open('inputs/day_6.txt', 'r') as txt:
        for line in txt.readlines():
            for num in line.strip().split(','):
                fish_dict[int(num)] += 1

    def run(input_dict, days):
        ret = input_dict
        for _ in range(days):
            new_dict = defaultdict(int)
            for remaining_cycle, fish_count in ret.items():
                if remaining_cycle == 0:
                    new_dict[8] += fish_count  # new fish
                    new_dict[6] += fish_count  # mother reset
                else:
                    new_dict[remaining_cycle-1] += fish_count
            ret = new_dict
        return ret
    # Part 1
    part1 = run(fish_dict, days=80)
    print(sum(part1.values()))  # 366057
    part2 = run(fish_dict, days=256)
    print(sum(part2.values()))  # 1653559299811