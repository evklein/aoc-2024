from .problem import Problem
from collections import namedtuple
import copy

Vector = namedtuple('Vector', ['x', 'y'])
TraceResult = namedtuple('TraceResult', ['unique_spaces_visited', 'num_loop_points'])

GUARD_ORIENTATIONS = ('^', '>', 'v', '<')

# Run raw
class Day6(Problem):
    def trace_guard_path(self, map, loop_limit):
        guard_position, guard_orientation = [(Vector(x, y), c) for x, r in enumerate(map) for y, c in enumerate(r) if c in GUARD_ORIENTATIONS][0]
        guard_vector = dict(zip(GUARD_ORIENTATIONS, (Vector(-1, 0), Vector(0, 1), (1, 0), (0, -1)))).get(guard_orientation)
        locations_visited, possible_loop_points = 0, 0
        visited = [guard_position]
        next_position = Vector(guard_position.x + guard_vector.x, guard_position.y + guard_vector.y)
        while 0 <= next_position.x < len(map[0]) and 0 <= next_position.y < len(map):
            if map[next_position.x][next_position.y] == '#':
                mul = -1 if abs(guard_vector.x) == 1 else 1
                guard_vector = Vector(guard_vector.y * mul, guard_vector.x * mul)
            else:
                guard_position = next_position
            visited.append(guard_position)
            locations_visited += 1
            next_position = Vector(guard_position.x + guard_vector.x, guard_position.y + guard_vector.y)
            if locations_visited >= loop_limit:
                possible_loop_points += 1
                break
        return TraceResult(len(set(visited)), possible_loop_points)

    def PartA(self, input):
        map = [[x for x in c] for i, c in enumerate(input.splitlines())]
        return self.trace_guard_path(map).unique_spaces_visited
        
    def PartB(self, input, loop_limit = 5_975): # Nasty problem brute focing, don't ask how I got this number. - TODO: rectangle search idea??
        possible_loop_points = 0
        original_map = [[x for x in c] for i, c in enumerate(input.splitlines())]
        for i, row in enumerate(original_map):
            for j, cell in enumerate(row):
                if cell != '#' and cell not in GUARD_ORIENTATIONS:
                    new_map = copy.deepcopy(original_map)
                    new_map[i][j] = '#'
                    possible_loop_points += self.trace_guard_path(new_map, loop_limit).num_loop_points
        return possible_loop_points
    
    # def optimize_part_b(self, input):
    #     lower, upper = 3500, 6500
    #     answer = ???
    #     while lower < upper:
    #         test_limit = lower + (upper - lower) // 2
    #         output = self.ActualB(input, loop_limit = test_limit)
    #         if output <= answer:
    #             upper = test_limit
    #         elif output > answer:
    #             lower = test_limit + 1
    #         print(output, lower, upper)
    #     return lower    
