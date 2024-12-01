import numpy as np

def read_in_array(filename):
    with open('data\day12.txt') as f:
        ls = []
        for line in f:
            ls.append(list(line.strip()))
    arr = np.array(ls)
    return arr

def get_letter_position(arr, letter):

    location = np.argwhere(arr == letter)[0]
    coords = (location[0], location[1])
    return coords

def map_letters(x):
    if x == 'S':
        x='a'
    elif x == 'E':
        x='z'
    return ord(x)-96

def convert_array_to_heights(arr):
    applyall = np.vectorize(map_letters)
    num_array = applyall(arr)
    return num_array

def get_nodes(arr,coord, height):
    
    i = coord[0]
    j = coord[1]
    max_row = np.shape(arr)[0] -1
    max_col = np.shape(arr)[1] -1
    nodes =[]

    if i < max_row and (arr[i+1,j] > height or arr[i+1,j]>= height-1):
        nodes.append((i+1,j))
    
    if i > 0 and (arr[i-1,j] > height or arr[i-1,j]>= height-1):
        nodes.append((i-1,j))
    
    if j < max_col and (arr[i,j+1] > height or arr[i,j+1]>= height-1):
        nodes.append((i,j+1))
    
    if j > 0 and (arr[i,j-1] > height or arr[i,j-1]>= height-1):
        nodes.append((i,j-1))
    return nodes


def generate_graph_dict(arr):
    graph_dict ={}
    for idx, x in np.ndenumerate(arr):
        nodes = get_nodes(arr,idx,x)
        graph_dict[(idx[0],idx[1])] = nodes
    return graph_dict

def generate_starting_coords_list(arr, use_fixed_start):
    
    start_coords_list =[]
    if use_fixed_start:
        start_coords = get_letter_position(arr,'S')
        start_coords_list.append(start_coords)
    else:
        for idx, x in np.ndenumerate(arr):
            if x == 'S' or x=='a':
                start_coords_list.append((idx[0],idx[1]))

    return start_coords_list

def get_shortest_path(graph, start, goal):
 
    visited = []
    # keep track of nodes to be checked
    queue = [[start]]

    if start == goal:
        return 

    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in visited:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour in goal:
                    return new_path 
            # Add the node to the visited list
            visited.append(node)
    return 

def process(part):

    # for part 1 we use the given start point "S". For part 2 we consider 
    # both "S" and anywhere else with start point "a"
    if part == 'part 1':
        use_fixed_start = True
    elif part == 'part 2':
        use_fixed_start = False

    # read in array and convert to heights
    start_array = read_in_array('day12.txt')
    height_array = convert_array_to_heights(start_array)
   
    # Calculate the possible paths for each position
    # This has been ammended so it works when we start at the end
    graph_dict = generate_graph_dict(height_array)

    # get the start and end coords
    # start_coords_list will be a list of possible start coordinates 
    # (but will only contain one item, the given position, for part 1)
    start_coords_list = generate_starting_coords_list(start_array, use_fixed_start)
    end_coords = get_letter_position(start_array,'E')

    # We call the shortest path in reverse. i,e starting at the end point so it 
    # will work when we don't know the start point
    shortest=  get_shortest_path(graph_dict, end_coords,start_coords_list)

    print("The shortest path for ",part," is ",len(shortest)-1)
    return


process('part 1')
process('part 2')


