from collections import defaultdict


if __name__ == '__main__':
    token_dict = defaultdict(int)   # NNCB => {'NN': 1, 'NC': 1, 'CB': 1} double counting of elements handled at the end
    instructions = {}  # { keyword: what to add between them }

    # inputs
    with open('inputs/day_14.txt', 'r') as txt:
        for line in txt.readlines():
            if line.strip():
                if '->' in line:
                    source, dest = line.strip().split(' -> ')
                    instructions[source] = dest
                else:
                    polymer_string = line.strip()

    # init (load polymer string into token dict)
    tokens = [polymer_string[i:i+2] for i in range(len(polymer_string) - 1)]
    for i in range(len(tokens)):
        token_dict[tokens[i]] += 1

    # Run simulation
    for _ in range(40):  # Use 10 for part1, 40 for part2
        temp = defaultdict(int)
        for token, count in token_dict.items():
            if token in instructions:
                element = instructions[token]
                temp[token[0] + element] += count
                temp[element + token[1]] += count
            else:
                temp[token] += count
        token_dict = temp

    # Count elements
    element_counts = defaultdict(int)
    first_token = polymer_string[:2]
    for token, count in token_dict.items():
        if first_token == token:                # Input  AA AB BC CD DE
            element_counts[token[0]] += count   # Count  A_
        element_counts[token[1]] += count       # Count  _A _B _C _D _E
    # Display result
    max_element_count = max(list(element_counts.values()))
    min_element_count = min(list(element_counts.values()))
    print(max_element_count - min_element_count)  # part1: 3306 part2: 3760312702877

