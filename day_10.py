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
        corrupt = None
        for i, c in enumerate(line):
            if c in close_to_open.values():  # opening bracket
                stack.append(c)
            elif stack and stack.pop() != close_to_open[c]:  # Closing bracket with corruption
                corrupt = c
                break
            if stack and (i == len(line) - 1):  # finished processing but incomplete
                incompletes.append([open_to_close[c] for c in reversed(stack)])
        if corrupt:
            corrupts.append(corrupt)
    # Part 1
    print(sum([corrupt_scores[c] for c in corrupts]))  # 315693

    # Part 2
    part2 = []
    for incomplete in incompletes:
        score = 0
        for c in incomplete:
            score = 5 * score + incomplete_scores[c]
        part2.append(score)
    print(sorted(part2)[int(len(incompletes)/2)])  # 1870887234
