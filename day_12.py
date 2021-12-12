from collections import defaultdict


def gen_paths(part2=False):
    valid_paths = []
    explorer_stack = [('start', [], None)]  # Node, trailing path, visited small cave

    while explorer_stack:
        explore_node, trailing_path, small_cave_visited = explorer_stack.pop()
        if explore_node == 'end':  # Terminating condition: add valid path
            valid_paths.append(trailing_path + ['end'])
        else:
            for accessible_node in path_dict[explore_node]:  # Test accessible nodes
                if accessible_node.islower() and accessible_node in trailing_path:  # small cave encountered before
                    if part2 and small_cave_visited is None:  # Part2: 1 quota to visit a small cave twice
                        explorer_stack.append((accessible_node, trailing_path + [explore_node], accessible_node))
                else:  # Unexplored path: Add to the stack
                    explorer_stack.append((accessible_node, trailing_path + [explore_node], small_cave_visited))
    return valid_paths


if __name__ == '__main__':
    path_dict = defaultdict(list)
    # input
    with open('inputs/day_12.txt', 'r') as txt:
        for line in txt.readlines():
            source, dest = line.strip().split('-')
            for s, d in ( (source, dest), (dest, source) ):
                if s != 'end' and d != 'start':
                    path_dict[s].append(d)  # Bi-directional except start and end
    # Part 1
    paths = gen_paths(part2=False)
    print(len(paths))  # 3856

    # Part 2
    paths = gen_paths(part2=True)
    print(len(paths))  # 116692
