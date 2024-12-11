from .problem import Problem
from collections import namedtuple

PART_A_LIMIT = 25
PART_B_LIMIT = 75

# Run raw
class Day11(Problem):
    def __init__(self):
        self.stones_memo = [{} for _ in range(max(PART_A_LIMIT, PART_B_LIMIT))]

    def PartA(self, input):
        stones = list(map(int, input.split()))
        for i in range(PART_A_LIMIT):
            stones = self.blink_a(stones)
        return len(stones)

    def blink_a(self, stones):
        new_stones = []
        for i, stone in enumerate(stones):
            if stone == 0:
                new_stones.append(1)
                continue
            elif len(str(stone)) % 2 == 0:
                new_stones.extend(list(map(int,(
                    str(stone)[:len(str(stone)) // 2],
                    str(stone)[len(str(stone)) // 2:],
                    ))))
            else:
                new_stones.append(stone * 2024)
        return new_stones

    def PartB(self, input):
        stones = list(map(int, input.split()))
        solution = 0
        depth = 0
        for i, stone in enumerate(stones):
            solution += self.blink_b([stone])
        return solution

    def blink_b(self, stones, depth = 0):
        if depth == PART_B_LIMIT:
            return len(stones)
        
        num_stones = 0
        for i, stone in enumerate(stones):
            if stone in self.stones_memo[depth]:
                num_stones += self.stones_memo[depth][stone]
                continue

            next_value = 0
            if stone == 0:
                next_value += self.blink_b([1], depth + 1)
            elif len(str(stone)) % 2 == 0:
                next_value += self.blink_b(list(map(int, (
                    str(stone)[:len(str(stone)) // 2],
                    str(stone)[len(str(stone)) // 2:],
                ))), depth + 1)
            else:
                next_value += self.blink_b([stone * 2024], depth + 1)
            
            if stone not in self.stones_memo[depth]:
                self.stones_memo[depth][stone] = next_value
            num_stones += next_value
        return num_stones