"""
Advent of Code 2024
Day 2: Red-Nosed Reports 
Part 1:

The engineers are trying to figure out which reports are safe.
The Red-Nosed reactor safety systems can only tolerate levels
that are either gradually increasing or gradually decreasing.
So, a report only counts as safe if both of the following are true:

* The levels are either all increasing or all decreasing.
* Any two adjacent levels differ by at least one and at most three.

Part 2:
The Problem Dampener is a reactor-mounted module that lets the reactor
safety systems tolerate a single bad level in what would otherwise be
a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level
from an unsafe report would make it safe, the report instead counts as safe.

https://adventofcode.com/2024/day/2
"""

def get_input(filename) -> list:
    report_list = []

    with open(filename, 'r') as file:
        for line in file:
            report_list.append(list(map(int, line.strip().split())))

    return report_list

def is_safe(report):

    safe = True
    prev_level = 0
    max_diff = 3
    min_diff = 1

    for idx, level in enumerate(report):
        if idx == 0:
            prev_level = level
        else:    
            diff = level- prev_level
            prev_level = level
            if idx == 1:
                if abs(diff) >=1 and abs(diff) <=3:
                    if diff < 0:
                        max_diff = -1
                        min_diff = -3
            if diff > max_diff or diff < min_diff:
                safe = False
                break

    return safe, idx


def solve_part1(data) -> int:

    report_count = 0
    for report in data:
        if is_safe(report)[0]:
            report_count +=1    

    return report_count

def solve_part2(data) -> int:
    report_count = 0

    for report in data:
        safe, idx = is_safe(report)
        if safe:
            report_count += 1
        else:
            # Handle reports where idx is within the first 3 elements
            if idx <= 2:
                list_to_check = [
                [report[i] for i in range(len(report)) if i != remove_idx]
                for remove_idx in range(3)
                ]

                # Check if any of the new lists are safe
                if any(is_safe(lst)[0] for lst in list_to_check):
                    report_count += 1
  
            else:
                new_list = [report[i] for i in range(len(report)) if i != idx]
                if is_safe(new_list)[0]:
                    report_count += 1

    return report_count


def main() -> None:
    
    report_list = get_input('2024/data/day2.txt')
    report_count = solve_part1(report_list)
    report_count_amended = solve_part2(report_list)

    print(f"The answer to part 1 is: {report_count}")
    print(f"The answer to part 2 is: {report_count_amended}")


if __name__ == '__main__':
    main()
