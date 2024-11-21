import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description = "Advent of Code 2024")
    parser.add_argument("-d", type=str, help="Day of the challenge")
    parser.add_argument("-p", type=str, help="Part of the day's challenge")
    parser.add_argument("-t", action="store_true", help="Use test input")
    parser.add_argument("-i", type=str, help="Input file")
    args = parser.parse_args()
    print(args)

if __name__ == "__main__":
    main()