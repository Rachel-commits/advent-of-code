"""
Advent of Code 2022
Day 8: Treetop Tree House
Find the numble of visible trees and calculate the max
scenic score possible for any tree
https://adventofcode.com/2022/day/8
"""
import numpy as np

#for part 1
def set_visible_trees(input_arr, height_arr, plane, reverse):
    """
    Create the tree height array. For every row and column
    travel in both directions and set the height array to
    have a value of 1 if the tree is visible form the outside
    """
    i = 0
    j = 0
    if reverse is False:
        stop = 0
    elif plane == 'h':
        stop = input_arr.shape[0] - 1
    elif plane == 'v':
        stop = input_arr.shape[1] - 1

    for i, row in enumerate(input_arr):
        max_height = 0
        if reverse is False:
            for j, element in enumerate(row):
                if element> max_height or j == stop:
                    max_height = element
                    if plane =='h':
                        height_arr[i,j]=1
                    elif plane == 'v':
                        height_arr[j,i]=1
        else:
            for j, element in reversed(list(enumerate(row))):
                if element> max_height or j == stop:
                    max_height = element
                    if plane =='h':
                        height_arr[i,j]=1
                    elif plane == 'v':
                        height_arr[j,i]=1
    return height_arr

#part2
def get_scenic_score(input_arr):
    """
    For each tree in the height array calculate the
    scenic score of each tree and keep a record of the
    highest score to date.
    """
    xmax = input_arr.shape[0] - 1
    ymax = input_arr.shape[1] - 1
    highest_score = 0
    for (i, j), _ in np.ndenumerate(input_arr):
        if i> 0 and j>0 and i<xmax and j<ymax:
            right_score = 0
            left_score=0
            up_score=0
            down_score =0
            tree_score = 0

            for coord in range(j+1,ymax+1):
                right_score+=1
                if input_arr[i,coord] >= input_arr[i,j]:
                    break
            for coord in range(j-1,-1, -1):
                left_score+=1
                if input_arr[i,coord] >= input_arr[i,j]:
                    break
            for coord in range(i+1,xmax+1):
                down_score+=1
                if input_arr[coord,j] >= input_arr[i,j]:
                    break
            for coord in range(i-1,-1, -1):
                up_score+=1
                if input_arr[coord,j] >= input_arr[i,j]:
                    break

            tree_score = right_score*left_score*up_score*down_score
            if tree_score>highest_score:
                highest_score = tree_score
    return highest_score

def process_answers():
    """
    Read in the file and call the function to set the
    height array from all 4 directions. Calculate
    part 1 and part 2
    """
    with open(r'data\day8.txt', encoding ='UTF8') as file:
        tree_list = []
        for line in file:
            tree_list.append(list(map(int,list(line.strip()))))

    # Read into an array and initialise height array
    tree_arr = np.array(tree_list)
    height_arr =np.zeros((tree_arr.shape[0],tree_arr.shape[1]))

    height_arr = set_visible_trees(tree_arr,height_arr, 'h', False)
    height_arr = set_visible_trees(tree_arr,height_arr, 'h', True)
    height_arr = set_visible_trees(tree_arr.T,height_arr, 'v', False)
    height_arr = set_visible_trees(tree_arr.T,height_arr, 'v', True)

    print("The answer to part 1 is ",int(height_arr.sum()))
    print("The answer to part 2 is ",get_scenic_score(tree_arr))
    return

process_answers()
