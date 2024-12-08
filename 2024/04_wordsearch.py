"""
Advent of Code 2024
Day 4: Ceres Search
Part 1:
As the search for the Chief continues, a small Elf who lives
on the station tugs on your shirt; she'd like to know if you
could help her with her word search (your puzzle input). She
only has to find one word: XMAS.

This word search allows words to be horizontal, vertical,
diagonal, written backwards, or even overlapping other words.
It's a little unusual, though, as you don't merely need to find
one instance of XMAS - you need to find all of them. 

Take a look at the little Elf's word search. How many times
does XMAS appear?

Part 2:
Looking for the instructions, you flip over the word search to find
that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in
which you're supposed to find two MAS in the shape of an X

https://adventofcode.com/2024/day/4
"""


def get_input(filename) -> list[list[str]]:

    with open(filename, 'r') as file:
        array = [list(line.strip()) for line in file]

    return array

def traverse(grid: list[list[str]], i: int, j: int) -> int:

    xmas_count = 0

    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1),  # Down, Up, Right, Left
        (1, -1), (-1, -1), (1, 1), (-1, 1)  # Diagonals: Down-Left, Up-Left, Down-Right, Up-Right
    ]

    for dx, dy in directions:
        try:
            if (
                grid[i + dx][j + dy] == 'M' and
                grid[i + 2 * dx][j + 2 * dy] == 'A' and
                grid[i + 3 * dx][j + 3 * dy] == 'S'
            ):
                xmas_count += 1
        except IndexError:
            continue  # Skip out-of-bound checks
    
    return xmas_count

    
  
def traverse_mas(grid: list[list[str]], i: int, j: int) -> int:

    corners = [grid[i-1][j-1],
        grid[i-1][j+1],
        grid[i+1][j-1],
        grid[i+1][j+1]
    ]

    if all(corner in {'M', 'S'} for corner in corners) and \
        corners[0] != corners[3] and \
        corners[1] != corners[2]:
        return 1
    
    return 0

def solve_part1(grid: list[list[str]]) -> int:

    total_xmas_count = 0
    for i, row in enumerate(grid):
        for j, element in enumerate(row):
            if element == 'X':
                total_xmas_count += traverse(grid,i,j)

    return total_xmas_count

def solve_part2(grid: list) -> int:

    num_cols = len(grid[0])
    num_rows = len(grid)
    total_xmas_count = 0

    # Do not iterate on the outer rows and columns to avoid boundary issues
    for i in range(1, num_rows - 1):  
        for j in range(1, num_cols - 1): 
            if grid[i][j] == 'A':
                total_xmas_count += traverse_mas(grid, i, j)

    return total_xmas_count

def main() -> None:

    wordsearch = get_input('2024/data/day4.txt')

    part1_result = solve_part1(wordsearch)
    part2_result = solve_part2(wordsearch)

    print(f"The answer to part 1 is: {part1_result}")
    print(f"The answer to part 2 is: {part2_result}")

if __name__ == '__main__':
    main()