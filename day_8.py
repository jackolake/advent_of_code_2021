from collections import defaultdict
"""
    Represent the display as
        a	a	
    d			b
    d			b
        c	c	
    g			e
    g			e
        f	f	
        
    the heuristic look like this
        a	b	c	d	e	f	g	length	Matching condition
    0	*	*		*	*	*	*	6	    count6 & intersact fully with 7 (but not 4)
    1		*			*			2	    count2
    2	*	*	*			*	*	5	    count5 & intersact 2 with 4
    3	*	*	*		*	*		5	    count5 & intersact fully with 1
    4		*	*	*	*			4	    count4
    5	*		*	*	*	*		5	    count5 & intersact 3 with 4
    6	*		*	*	*	*	*	6	    count6 & else
    7	*	*			*			3	    count3
    8	*	*	*	*	*	*	*	7	    count7
    9	*	*	*	*	*	*		6	    count6 & intersact fully with 4
"""


def create_map(digits):
    lmap = defaultdict(list)
    dmap = defaultdict(set)
    # Categorize by length
    for encoded in digits:
        lmap[len(encoded)].append(set(encoded))
    # Create map for known length
    dmap[1], dmap[4], dmap[7], dmap[8] = lmap[2][0], lmap[4][0], lmap[3][0], lmap[7][0]
    # Create map for length 5
    for encoded in lmap[5]:
        if (encoded & dmap[1]) == dmap[1]:
            dmap[3] = encoded
        else:
            dmap[2 if (len(encoded & dmap[4]) == 2) else 5] = encoded
    # Create map for length 6
    for encoded in lmap[6]:
        if (encoded & dmap[4]) == dmap[4]:
            dmap[9] = encoded
        elif (encoded & dmap[7]) == dmap[7]:
            dmap[0] = encoded
        else:
            dmap[6] = encoded
    return dmap


if __name__ == '__main__':
    signal_patterns = []
    output_values = []
    # input
    with open('inputs/day_8.txt', 'r') as txt:
        for line in txt.readlines():
            tokens = line.strip().replace(' |', '').split(' ')
            signal_patterns.append(tokens[:10])
            output_values.append(tokens[-4:])

    part1, part2 = 0, 0
    for signal_pattern, output_value in zip(signal_patterns, output_values):
        m = create_map(signal_pattern)  # {digit: encoding}
        lookup = dict([(''.join(sorted(list(v))), k) for k, v in m.items()])
        decoded = [lookup[''.join(sorted(encoding))] for encoding in output_value]
        for num in decoded:
            if num in [1, 4, 7, 8]:
                part1 += 1
        part2 += int(''.join([str(c) for c in decoded]))

    print(part1)  # 519
    print(part2)  # 1027483
