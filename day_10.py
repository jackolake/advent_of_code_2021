from functools import reduce

open_to_close = {'(': ')', '[': ']', '{': '}', '<': '>'}
close_to_open = dict((v, k) for k, v in open_to_close.items())

corrupt_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
incomplete_scores = {')': 1, ']': 2, '}': 3, '>': 4}

if __name__ == '__main__':
    lines = []
    # input
    with open('inputs/day_10.txt', 'r') as txt:
        lines = [line.strip() for line in txt.readlines()]

    # Process each lines
    corrupts = []
    incompletes = []
    for line in lines:
        stack = []
        for i, c in enumerate(line):
            if c in close_to_open.values():  # opening bracket
                stack.append(c)
            elif stack and stack.pop() != close_to_open[c]:  # Closing bracket with corruption
                corrupts.append(c)
                break
            if (i == len(line) - 1) and stack:  # finished processing this line but incomplete
                incompletes.append([open_to_close[c] for c in reversed(stack)])
    # Part 1: calculate sum of corrupt scores
    print(sum([corrupt_scores[c] for c in corrupts]))  # 315693

    # Part 2: Calculate incomplete scores and get the median
    part2 = [reduce(lambda n1, n2: 5*n1 + n2, [incomplete_scores[c] for c in incomplete]) for incomplete in incompletes]
    print(sorted(part2)[int(len(part2)/2)])  # 1870887234
