from .problem import Problem
from collections import namedtuple

MoveVector = namedtuple('MoveVector', ['x', 'y'])
MOVE_VECTORS = [
    MoveVector(1, 0), # Right
    MoveVector(0, 1), # Up
    MoveVector(-1, 0), # Left
    MoveVector(0, -1) # Down
]

class Day10(Problem):
    def __init__(self):
        self.trail_end_locations = []

    def PartA(self, input):
        grid, trailheads = self.parse_input(input)
        return sum(self.get_num_full_paths(grid, 0, i, j, allow_duplicates = False) for i, j in trailheads)

    def PartB(self, input):
        grid, trailheads = self.parse_input(input)
        return sum(self.get_num_full_paths(grid, 0, i, j, allow_duplicates = True) for i, j in trailheads)

    def parse_input(self, input):
        grid = [[x for x in c] for i, c in enumerate(input.splitlines())]
        trailheads = [(i, j) for i, row in enumerate(grid) for j, grid_value in enumerate(row) if int(grid_value) == 0]
        return grid, trailheads
        
    def get_num_full_paths(self, grid, prev, x, y, allow_duplicates = False):
        full_paths_from_position = 0
        if prev == 0:
            self.trail_end_locations.clear()

        if not(0 <= x < len(grid) and 0 <= y < len(grid[0])):
            return 0

        if prev == 9:
            if (x, y) not in self.trail_end_locations:
                if not allow_duplicates:
                    self.trail_end_locations.append((x, y))
                return 1
            return 0

        for move_vector in MOVE_VECTORS:
            next_x, next_y = x + move_vector.x, y + move_vector.y
            try:
                next_grid_value = int(grid[next_x][next_y])
                full_paths_from_position += self.get_num_full_paths(grid, prev + 1, next_x, next_y, allow_duplicates) if next_grid_value == prev + 1 else 0
            except (IndexError, ValueError) as e:
                continue
        return full_paths_from_position