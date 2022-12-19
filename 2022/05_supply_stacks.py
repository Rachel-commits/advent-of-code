"""
Advent of Code 2022
Day 2: Supply Stacks
Calculate the final stack positions accoring to
the input file
https://adventofcode.com/2022/day/5
"""

def generate_input(input_line, list_output, row_num):
    """
    Get the crates from the input
    """
    new_list =list(input_line[1::4])
    for i, element in enumerate(new_list):
        if row_num == 1:
            col =[]
            list_output.append(col)
        if element!=' ':
            list_output[i].append(element)

    return list_output

def move_crates(input_line, list_output, method):
    """
    Get the instructions from the input file
    and move the crate according to the instructions
    """
    instructions = input_line.split()
    num_move = int(instructions[1])
    from_index = int(instructions[3])-1
    to_index = int(instructions[5])-1

    for i in range(num_move):
        crate = list_output[from_index].pop(0)

        # For part 1 the crates in a column are moved 1 at a time
        # for part 2 all the crates in a column are moved all at once
        if method == 'part1':
            position = 0
        elif method == 'part2':
            position = i

        list_output[to_index].insert(position,crate)

    return list_output

def processing(part):
    """
    Read in the file, moves the crates and construct
    the return string of the top crates of each column.
    """
    with open(r'data\day5.txt', encoding = 'utf8') as file:
        crate_input = []
        row = 1
        instruction_input = False
        answer =[]

        for line in file:
            if '[' in line and instruction_input is False:
                crate_input = generate_input(line,crate_input, row)

            elif 'move' in line:
                crate_input = move_crates(line,crate_input, part)
            row += 1

        # Get the top crate from all the columns
        for i in crate_input:
            answer.append(i[0])
        answer_string = ''.join(answer)

    return answer_string

print("The answer to part1 is ", processing('part1'))
print("The answer to part2 is ", processing('part2'))
