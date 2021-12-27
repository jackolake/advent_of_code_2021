from __future__ import annotations
from itertools import cycle, product
from collections import Counter
from functools import lru_cache

part2_roll_combinations = list(product((1, 2, 3), (1, 2, 3), (1, 2, 3)))  # (1, 1, 1), (1, 1, 2), ..., (3, 3, 3)
part2_dice_sum = Counter(sum(rolls) for rolls in part2_roll_combinations)


def get_new_position(current_position: int, moves: int) -> int:
    return (current_position + moves - 1) % 10 + 1  # from 1 to 10 only


def part1(positions: list[int]) -> tuple[int, int]:
    scores = [0, 0]
    dice = cycle(range(1, 101))
    dice_rolled = 0
    while True:
        for i in range(len(positions)):  # move for each player in 1 turn
            moves = next(dice) + next(dice) + next(dice)  # roll deterministic die 3 times
            positions[i] = get_new_position(positions[i], moves)
            scores[i] = scores[i] + positions[i]
            dice_rolled += 3
            if scores[i] >= 1000:
                return min(scores) * dice_rolled  # losing player scores * dice rolls


@lru_cache(maxsize=None)  # Use tuples because lru_cache requires hashable inputs
def part2(positions: tuple[int], scores=(0, 0), current_player=0) -> tuple[int, int]:
    wins = (0, 0)
    other_player = (current_player + 1) % 2
    for moves, universes in part2_dice_sum.items():
        next_pos = get_new_position(positions[current_player], moves)
        next_score = scores[current_player] + next_pos
        if next_score >= 21:  # terminating condition
            wins = (wins[0] + universes, wins[1]) if current_player == 0 else (wins[0], wins[1] + universes)
        else:
            next_wins = part2(positions=(next_pos, positions[1]) if current_player == 0 else (positions[0], next_pos),
                              scores=(next_score, scores[1]) if current_player == 0 else (scores[0], next_score),
                              current_player=other_player)
            wins = (wins[0] + next_wins[0] * universes, wins[1] + next_wins[1] * universes)
    return wins


if __name__ == '__main__':
    # inputs
    with open('inputs/day_21.txt', 'r') as txt:
        lines = [line.strip() for line in txt.readlines()]
        p1_pos = int(lines[0].split(' ')[-1])
        p2_pos = int(lines[1].split(' ')[-1])

    print(part1(positions=[p1_pos, p2_pos]))  # 853776
    print(part2(positions=(p1_pos, p2_pos)))  # 301304993766094
