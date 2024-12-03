from .problem import Problem
import re

class Day3(Problem):
    def PartA(self, input):
        operations = re.findall(r'mul\(\d+,\d+\)', input)
        return sum(x * y for x, y in [list(map(int, re.findall(r'\d+', op))) for op in operations])

    def PartB(self, input):
        operations = re.finditer(r'mul\(\d+,\d+\)', input)
        multipliers_dict = { # New Dictionary: k = index of op in input, v = parsed mutliplicand and multiplier
            match.start(): list(map(int, re.findall(r'\d+', match.group())))
            for match in operations
        }
        do_indices = [match.start() for match in re.finditer(r'do\(\)', input)]
        do_not_indices = [match.start() for match in re.finditer(r'don\'t\(\)', input)]

        solution = 0
        for original_index, (x, y) in multipliers_dict.items():
            relevant_dos = [0] + [x for i, x in enumerate(do_indices) if x < original_index]
            relevant_donts = [x for i, x in enumerate(do_not_indices) if x < original_index]
            closest_flip = max(relevant_dos + relevant_donts)
            solution += x * y if closest_flip in relevant_dos else 0
        return solution