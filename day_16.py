import math
from functools import reduce


class Node(object):  # Tree node
    def __init__(self, code, version, type, parent=None, childrens=[], value=0):
        self.code = code
        self.version = version
        self.type = type
        self.parent = parent
        self.childrens = childrens
        self.value = value


def hex_to_bin_packet(s):
    # binary number is padded with leading zeroes until its length is a multiple of four bits
    return bin(int(s, 16))[2:].zfill(len(s) * 4)


def read_packet(s, parent, message_limit=math.inf):  # substring, parent node, message_limit
    message_parsed = 0
    while message_parsed < message_limit and len(s) >= 6 and int(s, 2) != 0:
        packet_version = int(s[:3], 2)
        packet_type_id = int(s[3:6], 2)
        if packet_type_id == 4:  # literal value
            literal_string = s[6:]
            value_string = ''
            for i in range(int(math.ceil(len(literal_string) / 5))):
                current_bits = literal_string[i * 5: i * 5 + 5]  # Load 5 bits
                value_string = value_string + current_bits[1:]
                if current_bits[0] == '0':  # Stop after last bit
                    s = literal_string[(i + 1) * 5:]
                    break
            value = int(value_string, 2)
            node = Node(code=value_string, version=packet_version,
                        type=packet_type_id, parent=parent,
                        childrens=[], value=value)
        else:  # operator packet
            length_type_id = s[6]
            node = Node(code=s, version=packet_version, type=packet_type_id, parent=parent, childrens=[], value=0)
            if length_type_id == '0':  # next 15 bits = total length in bits of the sub-packets
                subpackets_length = int(s[7: 22], 2)
                read_packet(s[22:22 + subpackets_length], parent=node)
                s = s[22 + subpackets_length:]  # get rid of substring which is processed
            else:  # next 11 bits = number of sub-packets immediately contained
                num_of_packets = int(s[7: 18], 2)
                s = read_packet(s[18:], parent=node, message_limit=num_of_packets)
        # Increment message counter
        parent.childrens.append(node)
        message_parsed += 1
    return s


if __name__ == '__main__':
    # inputs
    with open('inputs/day_16.txt', 'r') as txt:
        hex_input = [line.strip() for line in txt.readlines()][0]
    bin_packet = hex_to_bin_packet(hex_input)
    root = Node(code=bin_packet, version=0, type=None, parent=None, childrens=[])

    # Parse input into tree
    read_packet(bin_packet, parent=root)
    root = root.childrens[0]  # Skip the dummy root

    # Tree traversal function
    def traverse(node, part1):
        if node.type == 4:  # Literal node
            return node.version if part1 else node.value
        # Operator node
        vals = [traverse(child, part1=part1) for child in node.childrens]
        if part1:
            return sum(vals) + node.version
        if node.type == 0:  # sum
            return sum(vals)
        elif node.type == 1:    # product
            return reduce(lambda x, y: x*y, vals)
        elif node.type == 2:
            return min(vals)
        elif node.type == 3:
            return max(vals)
        elif node.type == 5:
            return 1 if vals[0] > vals[1] else 0
        elif node.type == 6:
            return 1 if vals[0] < vals[1] else 0
        elif node.type == 7:
            return 1 if vals[0] == vals[1] else 0
        return 0

    # part1
    print(traverse(root, part1=True))  # 875
    # part2
    print(traverse(root, part1=False))  # 1264857437203
