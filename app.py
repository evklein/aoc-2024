import argparse
from problem_sets import *
import time

def main():
    args = parse_arguments()

    if args.runall:
        total_time_ms = 0
        raw_input_days = [2, 3]
        for i in range(0, 4):
            start_time_a = time.perf_counter()
            problem = days[i]()
            ### Part A
            start_time_a = time.perf_counter()
            sol_a = problem.PartA(open(f'inputs/{i + 1}/a').read() if i in raw_input_days else open(f'inputs/{i + 1}/a').readlines())
            end_time_a = time.perf_counter()
            total_time_ms += end_time_a - start_time_a
            print(f'Day {i} Part A: {(end_time_a - start_time_a) * 1000:.1f}ms, Solution: {sol_a}')
            ### Part B
            start_time_b = time.perf_counter()
            sol_b = problem.PartB(open(f'inputs/{i + 1}/b').read() if i in raw_input_days else open(f'inputs/{i + 1}/b').readlines())
            end_time_b = time.perf_counter()
            total_time_ms += end_time_b - start_time_b
            print(f'Day {i} Part B: {(end_time_b - start_time_b) * 1000:.1f}ms, Solution: {sol_b}')
        print(f'Total time: {total_time_ms * 1000:.1f}ms')
        return

    print_header(args.day, args.part, args.test, args.raw)
    problem = days[args.day - 1]()
    input_file = f'inputs/{args.day}/{args.part}' + ('_TEST' if args.test else '')
    with open(input_file, 'r') as file_contents:
        if args.part.lower() == 'a':
            start_time = time.perf_counter()
            solution = problem.PartA(file_contents.read() if args.raw else file_contents.readlines())
        elif args.part.lower() == 'b':
            start_time = time.perf_counter()
            solution = problem.PartB(file_contents.read() if args.raw else file_contents.readlines())
    end_time = time.perf_counter()
    elapsed_time_raw = end_time - start_time
    print_footer(solution, elapsed_time_raw)

def parse_arguments():
    parser = argparse.ArgumentParser(description = 'Advent of Code 2024')
    parser.add_argument('-d', '--day', type=int, help='Day of the challenge')
    parser.add_argument('-p', '--part', type=str, help='Part of the day\'s challenge')
    parser.add_argument('-t', '--test', action='store_true', help='Use test input')
    parser.add_argument('-r', '--raw', action='store_true', help='Take input raw, no new lines')
    parser.add_argument('-ra', '--runall', action='store_true', help='Run all days and parts')
    return parser.parse_args()

def print_header(day, part, test, raw):
    print(f'''{'#' * 30}
# Advent of Code 2024
# Day {day} / Part {part.upper()}
# Test Mode: {test}
# Input Mode (Rawness): {raw}''')

def print_footer(solution, elapsed_time_raw):
    print(f'''{'#' * 30}
# Time: {elapsed_time_raw * 1000:.1f}ms
{'-' * 30}
# Solution: {solution}
{'#' * 30}
''')

if __name__ == '__main__':
    main()