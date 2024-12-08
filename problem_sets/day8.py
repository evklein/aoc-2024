from .problem import Problem
from collections import defaultdict, namedtuple

Vector = namedtuple('Vector', ['x', 'y'])

# Run raw
class Day8(Problem):
    def PartA(self, input):
        map, antennaes = self.parse(input)
        antinode_locations = self.find_antinodes(map, antennaes)
        return len(set(antinode_locations))

    def PartB(self, input):
        map, antennaes = self.parse(input)
        antinode_locations = self.find_antinodes(map, antennaes, True)
        return len(set(antinode_locations))

    def parse(self, input):
        map = [[x for x in c] for i, c in enumerate(input.splitlines())]
        antennaes = defaultdict(list)
        for i in range(len(map)):
            for j, value in enumerate(map[i]):
                if value != '.':
                    antennaes[value].append(Vector(i, j))
        return map, antennaes
    
    def find_antinodes(self, map, antennaes, extrapolate = False):
        antinode_locations = []
        for antannae_frequency, antannae_coordinates in antennaes.items():
            for i in range(len(antannae_coordinates)):
                current_antannae_coordinates = antannae_coordinates[i]
                for j in range(len(antannae_coordinates)):
                    if i == j:
                        continue
                    
                    next_antannae_coordinates = antannae_coordinates[j]
                    direction = Vector(
                        next_antannae_coordinates.x - current_antannae_coordinates.x,
                        next_antannae_coordinates.y - current_antannae_coordinates.y
                    )
                    neg_direction = Vector(-direction.x, -direction.y)
                    map_bounds = Vector(len(map), len(map[0]))
                    
                    next_possible_antinode = Vector(current_antannae_coordinates.x + neg_direction.x, current_antannae_coordinates.y + neg_direction.y)
                    
                    antinode_locations.extend(self.test_antinodes(map_bounds, neg_direction, next_possible_antinode, extrapolate))
                    antinode_locations.extend(self.test_antinodes(map_bounds, direction, next_possible_antinode, extrapolate))

        return antinode_locations

    def test_antinodes(self, map_bounds, dir_vector, possible_antinode_coordinates, extrapolate):
        locations = []
        while 0 <= possible_antinode_coordinates.x < map_bounds.x and \
              0 <= possible_antinode_coordinates.y < map_bounds.y:
            locations.append(possible_antinode_coordinates)
            if not extrapolate:
                break
            possible_antinode_coordinates = Vector(possible_antinode_coordinates.x + dir_vector.x, possible_antinode_coordinates.y + dir_vector.y)
        return locations
