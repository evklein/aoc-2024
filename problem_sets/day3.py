from .problem import Problem
import re

class Day3(Problem):
    def PartA(self, input):
        operations = re.findall(r'mul\(\d+,\d+\)', input)
        return sum(x * y for x, y in [list(map(int, re.findall(r'\d+', op))) for op in operations])

    def PartB(self, input):
        operations = re.finditer(r'mul\(\d+,\d+\)', input)
        multipliers_dict = {
            match.start(): list(map(int, re.findall(r'\d+', match.group())))
            for match in operations
        }
        do_indices = [match.start() for match in re.finditer(r'do\(\)', input)]
        do_not_indices = [match.start() for match in re.finditer(r'don\'t\(\)', input)]

        solution = 0
        for original_index, (x, y) in multipliers_dict.items():
            do = True
            for i in range(original_index, 0, -1): # Search for last do or don't
                if i in do_indices:
                    break
                if i in do_not_indices:
                    do = False
                    break
            if do:
                solution += x * y
        return solution