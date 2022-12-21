"""
Advent of Code 2022
Day 17: Grove Positions
Calculating the new coordinates
https://adventofcode.com/2022/day/20
"""

def read_file(filename):
    """
    Read in the file and create the original list
    """
    output_list = []
    with open(filename, encoding ='utf8') as file:
        for line in file:
            output_list.append(int(line.replace('\n','')))
    return output_list

def move_items(original_list, current_pos_dict, num_iterations):
    """
    Loop through each item in the list, move and update the position
    of the moved and impacted items.
    """
    count = 0
    list_len = len(original_list)

    while count < num_iterations:

        # Loop through all items in original list to move
        for i, move_val in enumerate(original_list):
            # get index
            prev_pos  = current_pos_dict[i]

            # get the new position
            if prev_pos + move_val == 0:
                new_pos = list_len - 1

            elif prev_pos + move_val < 0:
                new_pos = list_len - 1-1*(abs(prev_pos+move_val)%(list_len-1))

            else:
                new_pos =(prev_pos + move_val) % (list_len -1)

            # TO DO - Improve this looping don't loop for everything
            # Only loop for the if statemnt as well as updating the current version
            # update the position of the others

            for orig_index in current_pos_dict.keys():
                #Update the index for the moved item
                if orig_index == i:
                    current_pos_dict[orig_index] = new_pos

                else:
                    # Update the indexes for the impacted items
                    curr_index = current_pos_dict[orig_index]

                    # Positive move resulting in greater position
                    # Everything inbetween decreases by 1
                    if move_val > 0 and prev_pos< new_pos:
                        if curr_index > prev_pos and curr_index <= new_pos:
                            current_pos_dict[orig_index] = curr_index - 1

                    # Positive move resulting in lesser position
                    # Everything inbetween increases by 1
                    elif move_val > 0 and new_pos < prev_pos:
                        if curr_index >= new_pos and curr_index <prev_pos:
                            current_pos_dict[orig_index] = curr_index + 1

                    # Negative move resulting in lesser position
                    # Everything inbetween increases by 1
                    elif move_val <0 and  new_pos< prev_pos:
                        if curr_index >= new_pos and curr_index < prev_pos:
                            current_pos_dict[orig_index] = curr_index + 1

                    # Negative move resulting in greater position
                    # Everything inbetween decreases by 1
                    elif move_val <0 and  new_pos > prev_pos:
                        if curr_index > prev_pos and curr_index <= new_pos:
                            current_pos_dict[orig_index] = curr_index - 1

        count +=1

    return current_pos_dict

def get_coord(position, current_pos_dict, original_list):
    """
    Given a position, Find the corresponding psotion
    coordinates after the 0 value in the list
    """
    position_coord =0
    list_len = len(original_list)
    orig_0 = original_list.index(0)
    current_0 = current_pos_dict[orig_0]
    position_current_index = (position + current_0) % (list_len)


    for orig, curr in current_pos_dict.items():
        if curr == position_current_index:
            position_coord = original_list[orig]
    return position_coord

def sum_coords(current_pos_dict, original_list):
    """
    Sum the 1000th, 2000th and 3000th position
    coords after the 0 value in the list.
    """

    coord_1000 = get_coord(1000,current_pos_dict, original_list)
    coord_2000 = get_coord(2000,current_pos_dict, original_list)
    coord_3000 = get_coord(3000,current_pos_dict, original_list)

    coord_sum = coord_1000 + coord_2000 + coord_3000

    return coord_sum

def solve_puzzle(part):
    """
    Run the code to solve the puzzle. For part 2
    The values in the originali list are multiplied by
    811589153 and the original list is iterated through 10
    times.
    """
    original_list = read_file(r'data\day20.txt')

    #Create a dictionary that maps the original index to the current index
    current_pos_dict ={}
    list_len = len(original_list)
    current_pos_dict =dict(zip(range(list_len), range(list_len)))

    if part == 'part1':
        current_pos_dict = move_items(original_list, current_pos_dict, 1)
        answer = sum_coords(current_pos_dict, original_list)
        print("The answer to part 1 is", answer)

    elif part == 'part2':
        original_list = [x * 811589153 for x in original_list]
        current_pos_dict = move_items(original_list, current_pos_dict, 10)
        answer = sum_coords(current_pos_dict, original_list)
        print("The answer to part 2 is", answer)


solve_puzzle('part1')
solve_puzzle('part2')
