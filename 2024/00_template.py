"""
Advent of Code 2024
Day X: <Puzzle Name>
Part 1: <Part 1 Description>
Part 2: <Part 2 Description>

https://adventofcode.com/2024/day/X
"""

def get_input(filename) -> list:

    data =[]
    with open(filename, 'r') as file:
        for line in file:
            data.append(list(line.strip()))
    return data

def solve_part1(data) -> int:
    result = 0
    return result

def solve_part2(data) -> int:
    result = 0
    return result

def main() -> None:
    data = get_input('2024/data/exampleX.txt')

    part1_result = solve_part1(data)
    part2_result = solve_part2(data)

    print(f"The answer to part 1 is: {part1_result}")
    print(f"The answer to part 2 is: {part2_result}")

if __name__ == '__main__':
    main()
