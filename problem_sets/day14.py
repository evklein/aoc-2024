from .problem import Problem
from collections import namedtuple

MAP_WIDTH = 101
MAP_HEIGHT = 103
SECONDS = 100

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Bot():
    def __init__(self, pos, vec):
        self.pos = pos
        self.vec = vec

    def __str__(self):
        return f'{self.pos.x},{self.pos.y} - moving at {self.vec.x},{self.vec.y}'

class Day14(Problem):
    def PartA(self, input):
        bots = []
        for line in input.splitlines():
            first_split = line.split('=')
            # print('first_split', first_split)
            pos = tuple(map(int, first_split[1].split()[0].split(',')))
            vec = tuple(map(int, first_split[2].split(',')))
            bots.append(Bot(Vector(pos[0], pos[1]), Vector(vec[0], vec[1])))
        
        # print('Initial State')
        # self.print_map(bots[0])
        for i in range(SECONDS):
            for b_idx, bot in enumerate(bots):
                bot.pos.x += bot.vec.x
                bot.pos.y += bot.vec.y
                # print(f'New coords (before adj.): {bot.pos.x},{bot.pos.y}')
                if bot.pos.x >= MAP_WIDTH:
                    bot.pos.x = bot.pos.x - MAP_WIDTH
                if bot.pos.x < 0:
                    bot.pos.x = MAP_WIDTH + bot.pos.x
                
                if bot.pos.y >= MAP_HEIGHT:
                    bot.pos.y = bot.pos.y - MAP_HEIGHT
                if bot.pos.y < 0:
                    bot.pos.y = MAP_HEIGHT + bot.pos.y
                # print(f'New coords (after adj.): {bot.pos.x},{bot.pos.y}')
                # print(f'After {i + 1} seconds')

        quadrant_1, quadrant_2, quadrant_3, quadrant_4 = 0, 0, 0, 0
        vertical_meridian = MAP_WIDTH // 2
        horizontal_meridian = MAP_HEIGHT // 2
        # print(vertical_meridian)
        # print(horizontal_meridian)
        # self.print_map(bots)
        for bot in bots:
            # print(bot)
            if bot.pos.x < vertical_meridian and bot.pos.y < horizontal_meridian:
                quadrant_1 += 1
            elif bot.pos.x > vertical_meridian and bot.pos.y < horizontal_meridian:
                quadrant_2 += 1
            elif bot.pos.x < vertical_meridian and bot.pos.y > horizontal_meridian:
                quadrant_3 += 1
            elif bot.pos.x > vertical_meridian and bot.pos.y > horizontal_meridian:
                quadrant_4 += 1
        print(quadrant_1, quadrant_2, quadrant_3, quadrant_4)
        return quadrant_1 * quadrant_2 * quadrant_3 * quadrant_4

    def print_map(self, bots):
        for i in range(MAP_HEIGHT):
            for j in range(MAP_WIDTH):
                found_bot = False
                for bot in bots:
                    if bot.pos.x == j and bot.pos.y == i:
                        print('#', end='')
                        found_bot = True
                        break
                if found_bot:
                    continue
                print('.', end='')
            print()

    def PartB(self, input_block):
        bots = []
        for line in input_block.splitlines():
            first_split = line.split('=')
            # print('first_split', first_split)
            pos = tuple(map(int, first_split[1].split()[0].split(',')))
            vec = tuple(map(int, first_split[2].split(',')))
            bots.append(Bot(Vector(pos[0], pos[1]), Vector(vec[0], vec[1])))

        count = 0
        while True:
            next_input = input('type')
            for b_idx, bot in enumerate(bots):
                bot.pos.x += bot.vec.x
                bot.pos.y += bot.vec.y
                # print(f'New coords (before adj.): {bot.pos.x},{bot.pos.y}')
                if bot.pos.x >= MAP_WIDTH:
                    bot.pos.x = bot.pos.x - MAP_WIDTH
                if bot.pos.x < 0:
                    bot.pos.x = MAP_WIDTH + bot.pos.x
                
                if bot.pos.y >= MAP_HEIGHT:
                    bot.pos.y = bot.pos.y - MAP_HEIGHT
                if bot.pos.y < 0:
                    bot.pos.y = MAP_HEIGHT + bot.pos.y
            print('-' * 50)
            self.print_map(bots)
            print('COUNT', count := count + 1)
            print('-' * 50)
