from .problem import Problem

class PlotSection():
    def __init__(self, x_pos, y_pos, plot_value, top_neighbor, right_neighbor, bottom_neighbor, left_neighbor):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.plot_value = plot_value
        self.top_neighbor = top_neighbor
        self.right_neighbor = right_neighbor
        self.bottom_neighbor = bottom_neighbor
        self.left_neighbor = left_neighbor

    def __str__(self):
        return f'Position({self.x_pos}, {self.y_pos}), Value({self.plot_value}), Top({self.top_neighbor is not None}), Right({self.top_neighbor is not None}), Bottom({self.top_neighbor is not None}), Left({self.top_neighbor is not None})'

class Day12(Problem):
    def __init__(self):
        self.plot_grid = []

    def PartA(self, input):
        grid = [[c for c in line] for line in input.splitlines()]

        self.plot_grid = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                self.try_neighbor(grid, grid[x][y], x, y)

        print(self.plot_grid[0][0])
        
    def try_neighbor(self, grid, plot_value, x, y):
        if not (0 <= x < len(grid)) or not (0 <= y < len(grid[0])):
            return None
        
        if grid[x][y] != plot_value:
            return None

        if self.plot_grid[x][y] is not None:
            return self.plot_grid[x][y]

        # Create a placeholder to mark this cell as being processed
        placeholder = PlotSection(x, y, plot_value, None, None, None, None)
        self.plot_grid[x][y] = placeholder

        # Recursively assign neighbors
        placeholder.top_neighbor = self.try_neighbor(grid, plot_value, x + 1, y)
        placeholder.right_neighbor = self.try_neighbor(grid, plot_value, x, y + 1)
        placeholder.bottom_neighbor = self.try_neighbor(grid, plot_value, x - 1, y)
        placeholder.left_neighbor = self.try_neighbor(grid, plot_value, x, y - 1)

        return placeholder

    def PartB(self, input):
        pass