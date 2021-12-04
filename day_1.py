if __name__ == '__main__':
    nums = list()
    # input
    with open('inputs/day_1.txt', 'r') as txt:
        for line in txt.readlines():
            nums.append(int(line))
    # part 1
    print(len([i for i in range(1, len(nums)) if nums[i] > nums[i-1]]))

    # part 2
    print(len([i for i in range(3, len(nums)) if nums[i] > nums[i-3]]))