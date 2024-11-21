import argparse
from problem_sets import *
import datetime

def main():
    args = parse_arguments()
    print_header(args.day, args.part, args.test)
    problem = days[args.day - 1]()
    input_file = f'inputs/{args.day}/{args.part}' + ('_TEST' if not args.test else '')
    with open(input_file, 'r') as file_contents:
        if args.part.lower() == 'a':
            solution = problem.PartA(file_contents.readlines())
        elif args.part.lower() == 'b':
            solution = problem.PartB(file_contents.readlines())
    print_footer(solution)

def parse_arguments():
    parser = argparse.ArgumentParser(description = 'Advent of Code 2024')
    parser.add_argument('-d', '--day', type=int, help='Day of the challenge')
    parser.add_argument('-p', '--part', type=str, help='Part of the day\'s challenge')
    parser.add_argument('-t', '--test', action='store_true', help='Use test input')
    return parser.parse_args()

def print_header(day, part, test):
    print(f'''{'#' * 30}
# Advent of Code 2024
# Day {day} / Part {part.upper()}
# Test Mode: {test}
{'#' * 30}''')

def print_footer(solution):
    print(f'''{"#" * 30}
# Solution: {solution}
{'#' * 30}
''')

if __name__ == '__main__':
    main()