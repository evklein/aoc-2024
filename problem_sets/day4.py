from .problem import Problem

A_INVERSIONS = [
    [(0, 1), (0, 2), (0, 3)], # Right
    [(0, -1), (0, -2), (0, -3)], # Left
    [(1, 0), (2, 0), (3, 0)], # Up
    [(-1, 0), (-2, 0), (-3, 0)], # Down
    [(1, 1), (2, 2), (3, 3)], # Up Right
    [(1, -1), (2, -2), (3, -3)], # Up Left
    [(-1, 1), (-2, 2), (-3, 3)], # Down Right
    [(-1, -1), (-2, -2), (-3, -3)], # Down Left
]

B_INVERSIONS = [
    [(1, -1), (-1, 1)],
    [(-1, 1), (1, -1)],
    [(-1, -1), (1, 1)],
    [(1, 1), (-1, -1)],
]

# Run raw
class Day4(Problem):
    def PartA(self, input):
        grid = [[c for c in line] for line in input.splitlines()]
        solution = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 'X':
                    solution += sum([1 if self.test_inversion(grid, i, j, inv, 'MAS') else 0 for inv in A_INVERSIONS])
        return solution

    def test_inversion(self, grid, i, j, inversion, test_string):
        for k in range(len(test_string)):
            i_idx = i + inversion[k][0]
            j_idx = j + inversion[k][1]
            if not (0 <= i_idx < len(grid) and 0 <= j_idx < len(grid[i_idx])):
                return False
            elif grid[i_idx][j_idx] != test_string[k]:
                return False
        return True

    def PartB(self, input):
        grid = [[c for c in line] for line in input.splitlines()]
        return sum(
            1 if sum(
                1 if self.test_inversion(grid, i, j, inv, 'MS') else 0
                for inv in B_INVERSIONS
            ) >= 2 else 0
            for i, row in enumerate(grid)
            for j, char in enumerate(row)
            if char == 'A'
        )
