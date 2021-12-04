if __name__ == '__main__':
    op_list = list()
    # input
    with open('inputs/day_2.txt', 'r') as txt:
        for line in txt.readlines():
            op, num = line.split(' ')
            op_list.append((op, int(num)))
    # part 1
    horizontal, depth = 0, 0
    for op, num in op_list:
        if op == 'forward':
            horizontal += num
        else:
            depth += num if op == 'down' else -num
    print(horizontal*depth)

    # part 2
    horizontal, aim, depth = 0, 0, 0
    for op, num in op_list:
        if op == 'forward':
            horizontal += num
            depth += aim*num
        else:
            aim += num if op == 'down' else -num
    print(horizontal*depth)
