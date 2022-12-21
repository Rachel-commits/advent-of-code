"""
Advent of Code 2022
Day 21: Monkey Math
Calculate the monkeys yell number
https://adventofcode.com/2022/day/21
"""

import re
from sympy import symbols, solve

def create_dictionaries(filename):
    """
    Read in file and creates the monkey dictionaries
    """
    with open(filename, encoding='utf8') as file:
        number_dict = {}
        op_dict = {}
        for line in file:
            line = line.replace('\n','')
            monkey = line.split(':')[0]
            instruction = line.split(':')[1]

            # If number add to number dictionary
            if  all(num.isdigit() for num in instruction):
                number_dict[monkey] = int(instruction)
            else:
                op_dict[monkey] = instruction.split()

    return number_dict, op_dict


def construct_formula(formula, op_dict, number_dict, replace_humn):
    """
    Construct the formula from the monkey dictionaries.
    Option to replace humn with X for part 2.
    This function loops through and constructs the equation
    until all the monkey have been replaced
    """
    while re.search(r'[a-z]', formula):
        monkey_list = formula.split()

        for monkey in monkey_list:

            if re.search(r'[a-z]', monkey):
                if monkey =='humn' and replace_humn:
                    monkey_lookup = 'X'
                elif monkey in number_dict:
                    monkey_lookup = str(number_dict[monkey])
                elif monkey in op_dict:
                    monkey_lookup = '( ' + ' '.join(op_dict[monkey]) + ' )'

                formula = formula.replace(monkey, monkey_lookup)
                break
    return formula


def solve_puzzle():
    """
    Code to return the puzzle answers
    """
    #Part 1
    number_dict, op_dict = create_dictionaries(r'data\day21.txt')
    eqn = construct_formula('root',op_dict, number_dict, False)
    part1 = int(eval(eqn))
    print("The answer to part 1 is ", part1)

    #Part2
    eq1 = construct_formula(op_dict['root'][0], op_dict, number_dict, True)
    eq2 = construct_formula(op_dict['root'][2], op_dict, number_dict,True)

    symbol_x = symbols('X')
    zero_eq = eq1+'-'+eq2
    part2 = solve(zero_eq, symbol_x)[0]
    print("The answer to part 2 is ", part2)


solve_puzzle()
