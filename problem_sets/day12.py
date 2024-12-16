from .problem import Problem

class PlotSection():
    def __init__(self, x_pos, y_pos, plot_value):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.plot_value = plot_value
    
    def __str__(self):
        return f'({self.x_pos}, {self.y_pos}, {self.plot_value})'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, PlotSection):
            return (self.x_pos == other.x_pos and
                    self.y_pos == other.y_pos and
                    self.plot_value == other.plot_value)
        return False

    def __hash__(self):
        return hash((self.x_pos, self.y_pos, self.plot_value))
class Day12(Problem):
    def __init__(self):
        self.plot_grid = []

    def PartA(self, input):
        grid = [[c for c in line] for line in input.splitlines()]


        self.plot_grid = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]
        plot_set = set()
        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                plot_set.add(self.get_neighbors(grid, grid[x][y], x, y))

        # sum = 0
        # plot_groups = set()
        # for x, row in enumerate(self.plot_grid):
        #     for y, cell in enumerate(row):
        #         sum += 1 if cell.top_neighbor is None else 0
        #         sum += 1 if cell.right_neighbor is None else 0
        #         sum += 1 if cell.bottom_neighbor is None else 0
        #         sum += 1 if cell.left_neighbor is None else 0
        #         # print(cell)
        return sum
        
    def get_neighbors(self, grid, plot_value, x, y):
        if not (0 <= x < len(grid)) or not (0 <= y < len(grid[0])):
            return None
        
        if grid[x][y] != plot_value:
            return None

        if self.plot_grid[x][y] is not None:
            return self.plot_grid[x][y]

        # Create a placeholder to mark this cell as being processed
        placeholder = PlotSection(x, y, plot_value)
        self.plot_grid[x][y] = placeholder

        # Recursively assign neighbors
        top_neighbors = self.get_neighbors(grid, plot_value, x - 1, y)
        right_neighbors = self.get_neighbors(grid, plot_value, x, y + 1)
        bottom_neighbors = self.get_neighbors(grid, plot_value, x + 1, y)
        left_neighbors = self.get_neighbors(grid, plot_value, x, y - 1)

    def PartB(self, input):
        pass