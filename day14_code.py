import numpy as np

def update_min_and_max(x,y,min_x,min_y,max_x,max_y):
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y
    if x < min_x:
        min_x = x
    if y < min_y:
        min_y = y
    return min_x, min_y, max_x, max_y

def get_rock_coord(item):
    x = int(item.split(',')[0])
    y = int(item.split(',')[1])
    return x,y

def construct_between_points(coord_list,x,y,xprev,yprev):
    # Calculate the rock coords beyween the given 2 coords
    if x == xprev:
        for a in range(min(yprev,y), max(yprev,y) + 1):
            coord = (x,a)
            if coord not in(coord_list):
                coord_list.append(coord)
    
    if y == yprev:
        for a in range(min(xprev,x), max(xprev,x) + 1):
            coord = (a,y)
            if coord not in(coord_list):
                coord_list.append(coord)
    return coord_list


def create_rock(rock_string, rock_coords,min_x,min_y,max_x,max_y, line_num):

    coord_list = rock_string.replace(' ','').strip('\n').split('->')
    # loop through all the coordinates in the line
    for i, item in enumerate(coord_list):
        # Set the  min and max values t the first coord in the first line only
        if line_num ==1 and i == 0:
            x, y = get_rock_coord(coord_list[i])
            min_x =x  
            min_y =y 
            max_x =x
            max_y = y
        
         # two points and update the min and max 
        else:
            x, y = get_rock_coord(coord_list[i])
               # For 2nd coord onwards in the list create the coords between the 2 points
            if i>0:
                xprev, yprev =get_rock_coord(coord_list[i-1])
                rock_coords = construct_between_points(rock_coords,x,y,xprev,yprev)
            #update the min and max
            min_x, min_y, max_x, max_y = update_min_and_max(x,y,min_x,min_y,max_x,max_y)            
    return rock_coords, min_x,min_y,max_x,max_y


def coords_to_array(coords_list, min_x,min_y,max_x,max_y):
    rock_array =np.zeros((max_y+3,max_x+100000))
    for coord in coords_list:
        rock_array[coord[1],coord[0]] = 1
    return rock_array

def pour_sand(rock_array, start_row, start_col,count_sand):
    
     # go down until blocked
    for row in range(start_row, rock_array.shape[0]):

        # travel down until blocked
        if rock_array[row,start_col] > 0:
            # check its not at the bottom
            if row >= rock_array.shape[0] -1:
                rock_array[row-1,start_col] = 2
                count_sand+=1
                return rock_array, row, start_col, count_sand 
            
            else:
                # if at left edge left try right
                if  start_col == 0:
                    # if can travel then call recursive
                    if rock_array[row,start_col+1] == 0:
                        rock_array,row, start_col,count_sand = pour_sand(rock_array, row, start_col+1,count_sand)
                        return rock_array,row,start_col, count_sand
                
                # if at right edge then return
                elif start_col == rock_array.shape[1] -1:
                    return rock_array,row,start_col, count_sand
                
                #else try left
                else:
                    #try left
                    if rock_array[row,start_col-1] == 0:
                        rock_array,row, start_col, count_sand = pour_sand(rock_array, row, start_col-1,count_sand)
                        return rock_array,row,start_col, count_sand
                    #else try right
                    elif rock_array[row,start_col+1] == 0:
                        rock_array,row, start_col,count_sand =pour_sand(rock_array, row, start_col+1,count_sand)
                        return rock_array,row,start_col, count_sand

                    rock_array[row-1,start_col] = 2
                    count_sand+=1
                    return rock_array,row,start_col, count_sand

    return rock_array,row,start_col, count_sand

def process_input(filename, puzzle_part):
    rock_coords = []
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    line_num=0
    with open (filename) as f:
        for line in f:
            line_num+=1
            rock_coords,min_x,min_y,max_x,max_y = create_rock(line, rock_coords, min_x,min_y,max_x,max_y,line_num)

    rock_array = coords_to_array(rock_coords,  min_x,min_y,max_x,max_y)
    # array is indexed based so we increment the start col by 1
    row = 0
    count_sand = 0

    if puzzle_part == 'part1':
        #part 1 continue until the sane dpours out the array i.e. sand reaches a depth below the array
        while row < (max_y + 1): 
            rock_array,row, col, count_sand = pour_sand(rock_array, 0 ,500,count_sand)

    elif puzzle_part == 'part2':
        # part 2
        # Construct the floor at a depth ot 2 below the highest coordinate
        rock_array[max_y+2,:] = 1
        # continue until the start position becomes blocked
        while rock_array[0,500] == 0:
            rock_array,row, col, count_sand = pour_sand(rock_array, 0 ,500,count_sand)

    return count_sand

count_sand = process_input('day14.txt',  'part1')
print("The answer to part 1 is ", count_sand)

count_sand = process_input('day14.txt',  'part2')
print("The answer to part 2 is ", count_sand)
