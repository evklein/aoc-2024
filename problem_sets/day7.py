from .problem import Problem
from collections import namedtuple

Operation = namedtuple('Operation', ['final', 'values'])

# Run raw
class Day7(Problem):
    def PartA(self, input):
        operations = [Operation(int(x), list(map(int, y.split()))) for x, y in [line.split(':') for line in input.splitlines()]]
        solution = 0
        # Create map of all possible operations using binary math

        operator_combinations = []
        for operation in operations:
            combinations = 2 ** (len(operation.values) - 1)
            operator_combinations.append([str(bin(i))[2:].rjust(len(operation.values) - 1, '0').replace('0', '*').replace('1', '+') for i in range(combinations)])

        for i, operation in enumerate(operations):
            for combination in operator_combinations[i]:
                val = operation.values[0]
                for j in range(len(operation.values) - 1):
                    val = eval(f'{val}{combination[j]}{operation.values[j + 1]}')
                solution += operation.final if val == operation.final else 0
        return solution
                    
    def b10_to_ternary(self, number):
        tern_string = ''
        if number == 0:
            return '0'

        while number > 0:
            tern_string += str(number % 3)
            number //= 3
        return tern_string[::-1]

    def PartB(self, input):
        operations = [Operation(int(x), list(map(int, y.split()))) for x, y in [line.split(':') for line in input.splitlines()]]
        # Create map of all possible operations using binary math

        print('hm')
        operator_combinations = []
        for operation in operations:
            combinations = 3 ** (len(operation.values) - 1)
            operator_combinations.append([
                self.b10_to_ternary(i).rjust(len(operation.values) - 1, '0') \
                    .replace('0', '*') \
                    .replace('1', '+') \
                    .replace('2', '|') \
                for i in range(combinations)
            ])
        print('hm2')
        
        solution = 0
        for i, operation in enumerate(operations):
            for combination in operator_combinations[i]:
                val = operation.values[0]
                for j in range(len(operation.values) - 1):
                    operator = combination[j]
                    if operator == '|':
                        val = int(f'{val}{operation.values[j + 1]}')
                    else:
                        val = eval(f'{val}{operator}{operation.values[j + 1]}')
                if val == operation.final:
                    print('Testing operation', operation, 'with combination', combination, 'yields', val)

                    solution += operation.final
                    break
        return solution