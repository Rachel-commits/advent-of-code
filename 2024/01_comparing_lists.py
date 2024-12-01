"""
Advent of Code 2024
Day 1: Historian Hysteria
Part 1: What is the total distance between your lists?
Part 2: Calculate a total similarity score by adding up
each number in the left list after multiplying it by the 
number of times that number appears in the right list.

https://adventofcode.com/2024/day/1
"""
from collections import Counter

def get_lists(filename: str) -> tuple[list[int], list[int]]:
    list1 = []
    list2 = []

    with open(filename, 'r') as file:
        for line in file:
            list1.append(int(line.split()[0]))
            list2.append(int(line.split()[1]))
    
    return list1, list2

def solve_part1(list1: list[int], list2: list[int]) -> int: 
    difference=0
    list1.sort()
    list2.sort()
    for idx, element in enumerate(list1):
        difference+= abs(list1[idx] - list2[idx])
    
    return difference

def solve_part2(list1: list[int], list2: list[int]) -> int: 
    similarity_score = 0
    score_dict = Counter(list2)

    for element in list1:
        if element in score_dict:
            similarity_score += element*score_dict.get(element)

    return similarity_score

def main() -> tuple[int, int]:
    list1, list2 = get_lists('2024/data/day1.txt')
    difference = solve_part1(list1, list2)
    score = solve_part2(list1, list2)

    print(f"The answer to part 1 is: {difference}")
    print(f"The answer to part 2 is: {score}")
    
if __name__ == '__main__':
    main()
