"""
Advent of Code 2024
Day 3: Mull It Ove
Part 1:
It seems like the goal of the program is just to multiply
some numbers. It does that with instructions like mul(X,Y),
where X and Y are each 1-3 digit numbers. For instance,
mul(44,46) multiplies 44 by 46 to get a result of 2024.
Similarly, mul(123,4) would multiply 123 by 4.

However, because the program's memory has been corrupted,
there are also many invalid characters that should be ignored,
even if they look like part of a mul instruction. Sequences
like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

Part 2:
As you scan through the corrupted memory, you notice that some
 of the conditional statements are also still intact. If you 
 handle some of the uncorrupted conditional statements in the
 program, you might be able to get an even more accurate result.

There are two new instructions you'll need to handle:

The do() instruction enables future mul instructions.
The don't() instruction disables future mul instructions.
Only the most recent do() or don't() instruction applies.
At the beginning of the program, mul instructions are enabled.

https://adventofcode.com/2024/day/3
"""
import re

def get_input(filename) -> str:

    with open(filename, 'r') as file:
        output_str =file.read()

    return output_str


def detect_do_and_dont(input_str: str):

    do_pattern = r'do'
    dont_pattern = r'don\'t' 
    
    do_matches = list(re.finditer(do_pattern, input_str))
    dont_matches = list(re.finditer(dont_pattern, input_str))
        
    if do_matches and dont_matches:
        last_do = do_matches[-1]
        last_dont = dont_matches[-1]
        
        if last_do.start() > last_dont.start():
            return True  # 'do' appears last
        else:
            return False  # 'don't' appears last
    
    # If only 'do' matches, return True (since 'do' is found)
    elif do_matches:
        return True
    
    # If only 'don't' matches, return False
    elif dont_matches:
        return False

    # If neither 'do' nor 'don't' is found, return None
    return None

def extract_two_integers(input_string: str) -> tuple:

    pattern = r'^\d+,\d+\)'  # Ensure the string starts with the first number
    match = re.search(pattern, input_string)
    
    if match:
        # Use regex groups to extract the two integers
        inner_pattern = r'(\d+),(\d+)\)'
        inner_match = re.match(inner_pattern, match.group())
        return int(inner_match.group(1)), int(inner_match.group(2))
    
    return None 


def solve_part1(input_str: str) -> bool:

    result=0
    element_list = input_str.split('mul')

    for element in element_list:
        if element[0] == '(':
            integers = extract_two_integers(element[1:])
            if integers:
                multiplication = integers[0]*integers[1]
                result += multiplication

    return result

def solve_part2(input_str: str) -> int:

    result=0
    is_do = True
    element_list = input_str.split('mul')

    for element in element_list:
        if element[0] == '(':
            integers = extract_two_integers(element[1:])
            if integers and is_do:
                multiplication = integers[0]*integers[1]
                result += multiplication
        # update the is_do flag
        do_result = detect_do_and_dont(element)

        if do_result is not None:
            is_do = do_result

    return result

def main() -> None:

    input_string = get_input('2024/data/day3.txt')

    part1_result = solve_part1(input_string)
    part2_result = solve_part2(input_string)

    print(f"The answer to part 1 is: {part1_result}")
    print(f"The answer to part 2 is: {part2_result}")

if __name__ == '__main__':
    main()