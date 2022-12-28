"""
Advent of Code 2022
Day 18: Boiling Boulders
Calculate the surface area
https://adventofcode.com/2022/day/18
"""
import operator
import numpy as np

def count_external_sides(arr):
    """
    Starting at the corner visit all possible spaces.
    Count edge if meet a cube
    """
    idx = (0,0,0)
    queue = [idx]
    visited = []
    ext_side_count = 0
    # Pad the array to ensure a border around the edge for the boundary
    padded = np.pad(arr, pad_width=1, constant_values = 0)

    while len(queue) > 0:
        # Get last index from the queue
        idx = queue.pop()

        # If the position hasn't been visited before then check the neighbours
        if idx not in visited:
            # Mark as visited
            visited.append(idx)

            # check all 3 dimensionss
            for axis in range(3):
                adjacency_list = [0,0,0]
                adjacency_list[axis] = 1

                pos_adj_idx = tuple(map(operator.add, idx, tuple(adjacency_list)))
                neg_adj_idx = tuple(map(operator.add, idx, tuple([x*-1 for x in  adjacency_list])))

                # If the new position is a cube then add to faces count o
                # otherwise mark position to visit
                if idx[axis] < padded.shape[axis] -1:
                    if padded[pos_adj_idx] == 1:
                        ext_side_count+=1
                    else:
                        queue.append(pos_adj_idx)

                if  idx[axis] > 0:
                    if padded[neg_adj_idx] == 1:
                        ext_side_count+=1
                    else:
                        queue.append(neg_adj_idx)

    print("The total number of external sides is",ext_side_count )

def process_file(filename):
    """
    Read in file and create a coordinate array
    """
    with open(filename, encoding='UTF8') as file:
        line_num = 0
        coord_list=[]
        max_axis = [0,0,0]
        min_axis = [0,0,0]

        for line in file:
            line_num +=1
            coord = list(map(int, line.strip('\n').split(',')))
            coord_list.append(coord)

            for i in range(3):
                # Set min and max axis
                if line_num ==1:
                    min_axis[i] = int(coord[i])
                elif int(coord[i])< min_axis[i]:
                    min_axis[i] = int(coord[i])
                if int(coord[i])> max_axis[i]:
                    max_axis[i] = int(coord[i])

                max_int = max(max_axis)
    coordinate_array = np.zeros(tuple([ max_int +1 for item in max_axis]))
    # coordinate_array = np.zeros(tuple([ item +1 for item in max_axis]))
    for coord in coord_list:
        coordinate_array[coord[0],coord[1],coord[2]] =1

    return coordinate_array

def count_along_index(idx, arr, axis):
    """
    Given the axis if possible increment position by -1 and +1,
    and if there is a cube add to the adjacency count
    """
    adj_count = 0
    adjacency_list = [0,0,0]

    # Create adjacency tuple
    for i in range(3):
        if i == axis:
            adjacency_list[i] = 1

    pos_adj_idx = tuple(map(operator.add, idx, tuple(adjacency_list)))
    neg_adj_idx = tuple(map(operator.add, idx, tuple([x*-1 for x in  adjacency_list])))

    if idx[axis] < arr.shape[axis] -1 :
        if arr[pos_adj_idx] == 1:
            adj_count += 1

    if  idx[axis] > 0:
        if arr[neg_adj_idx] == 1:
            adj_count+=1

    return adj_count

def count_sides(arr):
    """
    Count adjacent sides to determine sides that aren't connected
    to another cube to setrmine the surface area
    """
    cube_count = 0
    total_sides = 6
    tot_exposed_sides = 0

    # For each cube we check if there is an adjacent cubel along each axis
    for idx, cube in np.ndenumerate(arr):
        adj_sides = 0
        if cube == 1:
            cube_count+=1
            adj_sides+=count_along_index(idx, arr,0)
            adj_sides+=count_along_index(idx, arr,1)
            adj_sides+=count_along_index(idx, arr,2)

            #Surface area is the number of sides that aren't adjacent
            tot_exposed_sides+= total_sides - adj_sides

    print("The total number of exposed sides is", tot_exposed_sides)


def solve_puzzle():
    """
    Driver code to read in file and solve Part 1 and Part2
    """
    coordinate_array = process_file(r'data/day18.txt')
    count_sides(coordinate_array)
    count_external_sides(coordinate_array)

solve_puzzle()
