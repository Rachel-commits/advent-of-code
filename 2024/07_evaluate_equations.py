
"""
Advent of Code 2024
Day 7: Bridge Repair

Part 1:
Each line represents a single equation. The test value appears
before the colon on each line; it is your job to determine whether
the remaining numbers can be combined with operators to produce
the test value.
Operators are always evaluated left-to-right, not according to 
precedence rules. Furthermore, numbers in the equations cannot
be rearranged. Glancing into the jungle, you can see elephants
holding two different types of operators: add (+) and multiply (*).

Part 2:
The engineers seem concerned; the total calibration result you gave
them is nowhere close to being within safety tolerances. Just then,
you spot your mistake: some well-hidden elephants are holding a third
type of operator.
The concatenation operator (||) combines the digits from its left and
right inputs into a single number. For example, 12 || 345 would become
12345. All operators are still evaluated left-to-right.

https://adventofcode.com/2024/day/X
"""
import itertools

def get_input(filename: str) -> list:

    equations =[]

    with open(filename, 'r') as file:
        for line in file:
            split_line = line.strip().split(':')
            test_result = int(split_line[0])
           
            integer_list = list(map(int, split_line[1].strip().split()))
            equations.append(tuple([test_result, integer_list]))

    return equations

def get_operations_map(operator_list: list, length: int) -> list:
 
    # Generate all combinations
    combinations = list(itertools.product(operator_list, repeat=length))
    operations = [list(combination) for combination in combinations]

    return operations

def evaluate_operation(int1: int, int2: int, operator: str) -> int:

    if operator == '||':
        result = int(str(int1)+str(int2))
    else:
        result = eval(f"{int1} {operator} {int2}")

    return result


def solve_puzzle(equations:list, operators:list, already_passed:set) -> int:
    
    test_sum = 0
    test_passed_posns =[]

    # Loop through all the equations
    for idx, equation in enumerate(equations):
        if idx not in already_passed:
            # Get the test result and the integers
            test_result = equation[0]
            integers = equation[1]
            list_length = len(integers)
            test_passed = False

            # Get the list of all possible operations. If part 2 dont recheck * and + only
            if already_passed:
                operations = get_operations_map(operators, list_length-1)
                operations_list = [op for op in operations if '||' in op]
            else:
                operations_list = get_operations_map(operators, list_length-1)
    
            for operations in operations_list:

                # For each combination evaluate the result
                for i, int in enumerate(integers):
                    if i==0:
                        last_result = int
                    else:
                        operator =operations[-i]
                        last_result = evaluate_operation(last_result, int, operator)

                        if last_result > test_result:
                            break # exit the current operation list if we have exceeded the test
    
                    # Last result if last_result = test result
                    if i == list_length - 1:
                        if last_result == test_result:
                            test_passed = True
                            test_passed_posns.append(idx)
                            break # exit if we find a passing test

            if test_passed:
                test_sum += test_result
     
    return test_sum, set(test_passed_posns)

def main() -> None:
    equations = get_input('2024/data/day7.txt')

    part1_result, test_passed_posns = solve_puzzle(equations, ['*', '+'], {})
    part2_result, _ = solve_puzzle(equations, ['*', '+', '||'], test_passed_posns)
    total_passes = part1_result + part2_result
    
    print(f"The answer to part 1 is: {part1_result}")
    print(f"The answer to part 2 is:  {total_passes}")


if __name__ == '__main__':
    main()
