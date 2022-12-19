"""
Advent of Code 2022
Day 2: Rock Paper Scissors
Calculating the score of rock paper scissors
https://adventofcode.com/2022/day/2
"""

def part1(mine, opponent):
    """
    Given the 2 moves calculate the scores
    according to the part 1 rules
    """

    score = 0

    if mine == 'X':
        score+=1
        if opponent == 'A':
            score+=3
        elif opponent == 'C':
            score+=6

    elif mine == 'Y':
        score+=2
        if opponent == 'B':
            score+=3
        elif opponent == 'A':
            score+=6

    elif mine == 'Z':
        score+=3
        if opponent == 'C':
            score+=3
        elif opponent == 'B':
            score+=6

    return score

def part2(mine, opponent):
    """
    Given the 2 moves calculate the scores
    according to the part 2 rules
    """

    score = 0
    if mine == 'X':
        if opponent == 'A':
            score+=3
        elif opponent == 'B':
            score+=1
        elif opponent == 'C':
            score+=2

    elif mine == 'Y':
        score+=3
        if opponent == 'A':
            score+=1
        elif opponent == 'B':
            score+=2
        elif opponent == 'C':
            score+=3

    elif mine == 'Z':
        score+=6
        if opponent == 'A':
            score+=2
        elif opponent == 'B':
            score+=3
        elif opponent == 'C':
            score+=1

    return score

def run_puzzle(filename):
    """
    Read in file and calulate the scores
    for part 1 and part 2.
    """

    part1_score = 0
    part2_score = 0

    with open(filename, encoding= 'utf8') as file:

        for line in file:
            test = line.split()
            opponent = test[0]
            mine = test[1]

            part1_score += part1(mine, opponent)
            part2_score += part2(mine, opponent)

    print("The answer to part 1 is ", part1_score)
    print("The answer to part 2 is ", part2_score)

run_puzzle(r'data\day2.txt')
