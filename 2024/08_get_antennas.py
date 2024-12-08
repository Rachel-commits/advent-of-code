"""
Advent of Code 2024
Day 8: Resonant Collinearity

How many unique locations within the bounds of the map contain an antinode?

Part 1: 
The signal only applies its nefarious effect at specific antinodes based on the
resonant frequencies of the antennas. In particular, an antinode occurs at any
point that is perfectly in line with two antennas of the same frequency - but 
only when one of the antennas is twice as far away as the other. This means 
that for any pair of antennas with the same frequency, there are two antinodes,
one on either side of them.

Part 2:
it turns out that an antinode occurs at any grid position exactly in line with 
at least two antennas of the same frequency, regardless of distance. This means
that some of the new antinodes will occur at the position of each antenna
(unless that antenna is the only one of its frequency).

https://adventofcode.com/2024/day/8
"""
import itertools

def get_input(filename: str) -> list:

    grid =[]
    with open(filename, 'r') as file:
        for line in file:
            grid.append(list(line.strip()))

    return grid

def create_freq_dict(grid: list) -> dict:

    freq_dict = {}
    for i, row in enumerate(grid):
        for j, element in enumerate(row):
            if element =='.':
                continue
            else:
                if element not in freq_dict:
                    freq_dict[element] = []
                freq_dict[element].append((i, j))
    return freq_dict

def calc_diff(pair: tuple) -> tuple:

    row_diff = pair[0][0] - pair[1][0]
    col_diff = pair[0][1] - pair[1][1]
    
    return row_diff, col_diff

def apply_move(posn: tuple, row_diff: int, col_diff:int) -> tuple:
    return posn[0] + row_diff, posn[1] + col_diff

def check_bounds(posn: tuple, num_rows:int, num_cols:int) -> bool:
    return 0 <= posn[0] < num_rows and 0 <= posn[1] < num_cols

def get_antinodes(pair: list, row_diff: int, col_diff: int, num_rows: int, num_cols: int, loop_all=False) -> set:
    
    positions = set()

    # Loop through the pair of coordinates
    for i, coords in enumerate(pair):
        # Reverse the direction of row_diff and col_diff for the second coords in the pair
        if i == 1:
            row_diff = -row_diff
            col_diff = -col_diff

        last_posn = coords

        # Apply the move until out of bounds, either once or multiple times based on loop_all flag
        while True:
            new_posn = apply_move(last_posn, row_diff, col_diff)
            if check_bounds(new_posn, num_rows, num_cols):
                positions.add(new_posn)
                last_posn = new_posn
                if not loop_all:
                    break  # Stop if we're not looping (for part 1)
            else:
                break  # Break if out of bounds

    return positions

def solve_puzzle(grid:list, is_part2:bool) -> int:

    antinodes = set()
    num_rows = len(grid)
    num_cols = len(grid[0])
    freq_dict = create_freq_dict(grid)
    loop_all = is_part2 # true for part 2
    add_antennas  = is_part2 # true for part 2

    #  Loop through all the differeing antennas
    for key in freq_dict:
        pair_list = freq_dict[key]

        # Only continue if we have at least 2 coordinates for the antenna
        if len(pair_list) > 1:
            pairs = list(itertools.combinations(pair_list, 2))
            # For each combination of pairs locate the antinodes
            for pair in pairs:
                row_diff, col_diff = calc_diff(pair)
                positions = get_antinodes(pair, row_diff, col_diff, num_rows, num_cols, loop_all) 
                # Add the antinode positions to the set
                antinodes.update(positions)
                # For part 2 we also add add coordinates of the antenna    
                if add_antennas:
                    antinodes.add(pair[0])
                    antinodes.add(pair[1])

    return len(antinodes)

def main() -> None:
    grid = get_input('2024/data/day8.txt')

    # part1_result = solve_part1(grid)
    # part2_result = solve_part2(grid)
    part1_result = solve_puzzle(grid, False)
    part2_result = solve_puzzle(grid, True)
    # # 259 927
    print(f"The answer to part 1 is: {part1_result}")
    print(f"The answer to part 2 is: {part2_result}")

if __name__ == '__main__':
    main()



