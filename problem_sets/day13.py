from .problem import Problem
from collections import namedtuple

Vector = namedtuple('Vector', ['x', 'y'])
Machine = namedtuple('Machine', ['a_vector', 'b_vector', 'prize_pos'])

class Day13(Problem):
    def parse_input(self, input, adjustment = 0):
        machines = []
        lines = input.splitlines()
        for i in range(0, len(lines), 4):
            first_split_a = lines[i].split('+')
            a_vector = Vector(int(first_split_a[1].split(',')[0]), int(first_split_a[2]))
            first_split_b = lines[i + 1].split('+')
            b_vector = Vector(int(first_split_b[1].split(',')[0]), int(first_split_b[2]))
            first_split_prize = lines[i + 2].split('=')
            prize_pos = Vector(int(first_split_prize[1].split(',')[0]) + adjustment, int(first_split_prize[2]) + adjustment)
            machines.append(Machine(a_vector, b_vector, prize_pos))
        return machines
    
    def calculate_linear_system_for_machines(self, machines):
        solution = 0
        for (a_vector, b_vector, prize_pos) in machines:
            x_1 = a_vector.x
            y_1 = b_vector.x
            c_1 = prize_pos.x

            x_2 = a_vector.y
            y_2 = b_vector.y
            c_2 = prize_pos.y

            new_x_1 = x_2 * x_1
            new_y_1 = x_2 * y_1
            new_c_1 = x_2 * c_1

            new_x_2 = x_1 * x_2
            new_y_2 = x_1 * y_2
            new_c_2 = x_1 * c_2

            final_x = (new_c_2 - new_c_1) / (new_y_2 - new_y_1)
            final_y = (c_1 - y_1 * final_x) / x_1

            solution += int(final_x + final_y * 3) if final_x % 1 == 0 and final_y % 1 == 0 else 0
        return solution

    def PartA(self, input):
        machines = self.parse_input(input)
        return self.calculate_linear_system_for_machines(machines)

    def PartB(self, input):
        machines = self.parse_input(input, 10000000000000)
        return self.calculate_linear_system_for_machines(machines)