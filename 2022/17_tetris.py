"""
Advent of Code 2022
Day 17: Pyroclastic Flow
Calculating the height of the rocks
https://adventofcode.com/2022/day/17
"""

from collections import Counter

def get_rock_vertices(rock_num, floor_height):
    """
    From the number of the rock. Calculate its
    starting coordinates depending on shape type
    """
    coordinate_list = []

    # minus
    if rock_num % 5 == 1:
        coordinate_list.append((3, floor_height + 4))
        coordinate_list.append((4, floor_height + 4))
        coordinate_list.append((5, floor_height + 4))
        coordinate_list.append((6, floor_height + 4))

    # plus
    elif rock_num % 5 == 2:
        coordinate_list.append((4, floor_height + 4))
        coordinate_list.append((3, floor_height + 5))
        coordinate_list.append((4, floor_height + 5))
        coordinate_list.append((5, floor_height + 5))
        coordinate_list.append((4, floor_height + 6))

    #L
    elif rock_num % 5 == 3:
        coordinate_list.append((3, floor_height + 4))
        coordinate_list.append((4, floor_height + 4))
        coordinate_list.append((5, floor_height + 4))
        coordinate_list.append((5, floor_height + 5))
        coordinate_list.append((5, floor_height + 6))

    #I
    elif rock_num % 5 == 4:
        coordinate_list.append((3, floor_height + 4))
        coordinate_list.append((3, floor_height + 5))
        coordinate_list.append((3, floor_height + 6))
        coordinate_list.append((3, floor_height + 7))

    # square
    elif rock_num % 5 == 0:
        coordinate_list.append((3, floor_height + 4))
        coordinate_list.append((3, floor_height + 5))
        coordinate_list.append((4, floor_height + 4))
        coordinate_list.append((4, floor_height + 5))

    return coordinate_list

def can_rock_move_horizontal(rock, jet, chamber):
    """
    Given a rocks coordinates check if it is
    possible to move 1 position horizontally
    in a direction determined by the jet
    """
    for coord in rock:
        coord = (coord[0] + jet, coord[1])
        if coord in chamber:
            return False
        elif coord[0]<1 or coord[0]>7:
            return False
    return True

def can_rock_move_down (rock,chamber):
    """
    Given a rocks coordinates check if it is
    possible to move down 1 position
    """
    for coord in rock:
        coord = (coord[0], coord[1]-1)
        if coord in chamber:
            return False
        elif coord[1] == 0:
            return False
    return True

def simulate_fall(jet_list,rock, chamber, floor_height,jet_position):
    """
    Generate the rocks fall. Gets the jets position, checks
    if it is possible for the rock to move horizontally and down. If
    so moves the rock. Update the floor height and the list of existing
    positions
    """
    jet_max_pos = len(jet_list) -1
    blocked = False

    while blocked is False:
        # First try the jet move and move if possible
        jet = jet_list[jet_position]
        if can_rock_move_horizontal(rock, jet, chamber):
            rock = [(coord[0] + jet, coord[1]) for coord in rock]

        # increment the jet position for next time restart list if end is reached
        if jet_position == jet_max_pos:
            jet_position = 0
        else:
            jet_position +=1

        #Then move down if possible
        if can_rock_move_down(rock,chamber):
            rock = [(coord[0], coord[1]-1) for coord in rock]

        # The rock comes to rest and add the final coords the the chamber map
        else:
            for coord in rock:
                chamber.append(coord)
                if coord[1] > floor_height:
                    floor_height = coord[1]
            blocked = True
    return chamber, floor_height, jet_position

def get_jet_pattern(filename):
    """
    Converts the input file jetstream to
    1 for > and -1 for <
    """
    with open(filename, encoding = 'utf8') as file:
        for line in file:
            line = list(line)
            jet_list = [1 if item == '>' else -1 for item in line]

    return jet_list

def reset_floor(chamber, floor_height, master_floor_height):
    """
    Once the floor is complete this function removes everything
    below it from the chamber coordinates and resets the floor
    height variable but stores the running total of the actual floor
    height. I initially tried this for part 2 but did not use
    in the end. """

    key_list =[]

    xcoord, ycoord = zip(*chamber)
    counter = Counter(ycoord)

    for key, value in counter.items():
        if value==7:
            key_list.append(key)

    if  key_list:
        new_floor = max(key_list)
        for coord in chamber.copy():
            if coord[1] <= new_floor:
                chamber.remove(coord)

        chamber = [(coord[0], coord[1]-new_floor) for coord in chamber]
        floor_height -=new_floor
        master_floor_height += new_floor

    return master_floor_height, floor_height, chamber

def pattern_repeat(state_dict):
    """
    This function looks to find the repeat pattern
    of the fallen ricks by checking the state
    dictionary. Note we remove the floor height from
    the state check as this will always be different.
    We are just checking the rock type, the jet flow
    and the height increment
    """
    initial_key = 300
    initial_state = state_dict[initial_key]
    # Loop through each record in the state dictionary after the
    # initial check until the same state is found and check this
    # repeat cycle
    for key, state_list in state_dict.items():
        if key > initial_key:
            if state_list[:3] == initial_state [:3]:
                repeat = key - initial_key
                found = True
                # Once the state has been found for the first time
                # ensure all other states in the calculated repeat
                # pattern also match. If they don't then we return
                # to the initial loop to find the next repeat

                for i in range(repeat):
                    i += 1
                    if state_dict.get(key + i,[])[:3] == state_dict.get(initial_key + i ,[])[:3]:
                        continue
                    else:
                        found = False
                        break
                if found:
                    return repeat
    return 0

def process_rocks(num_of_rocks, filename):
    """
    Loop throuh all the rocks and update the chamber,
    row height and state dictionary after a fall
    """
    chamber = []
    floor_height =0
    jet_position =0
    state_dict ={}

    jet_list = get_jet_pattern(filename)

    for i in range(num_of_rocks):
        state_list =[]
        rock_number = i+1
        prev_floor_height = floor_height
        
        rock_coords = get_rock_vertices(rock_number, floor_height)

        chamber, floor_height, jet_position = simulate_fall(
                                                jet_list,
                                                rock_coords,
                                                chamber,
                                                floor_height,
                                                jet_position
                                                )
        # Create a state list containing the rock_type, the jet position
        # and the floor increment of the latest round
        state_list.append(rock_number % 5)
        state_list.append(jet_list[jet_position])
        state_list.append(floor_height-prev_floor_height)
        state_list.append(floor_height)
        state_dict[rock_number] = state_list

    return floor_height, state_dict

def get_rock_height_formula(num_rocks, state_dict):
    """
    This function uses the pattern repeat to create
    the formula coefficients and then to calculate
    the final row height
    """

    # Find the pattern repeat
    repeat = pattern_repeat(state_dict)

    divisor = num_rocks // repeat
    remainder = num_rocks % repeat

    repeat_coeff = state_dict[repeat][3]
    diff_coeff = state_dict[2*repeat][3] - repeat_coeff
    mod_coeff = state_dict[repeat + remainder][3] - repeat_coeff

    row_height = repeat_coeff + diff_coeff*(divisor - 1) + mod_coeff

    return row_height

# Run initial code for 5000 rocks
state = process_rocks(5000, r'data\day17.txt')[1]
height_pt1 = state[2022][3]
height_pt2 = get_rock_height_formula(1000000000000, state)

print("The floor height after 2022 rocks is ", height_pt1)
print("The floor height after 1000000000000 rocks is ", height_pt2)
