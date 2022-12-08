import numpy as np

#for part 1
def set_visible_trees(input_arr,height_arr, plane, reverse):
    i = 0
    j = 0
    if reverse == False:
        stop = 0
    elif plane == 'h':
        stop = input_arr.shape[0] - 1
    elif plane == 'v':
        stop = input_arr.shape[1] - 1

    
    for i, row in enumerate(input_arr):
        max_height = 0
        if reverse == False:
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

    xmax = input_arr.shape[0] - 1
    ymax = input_arr.shape[1] - 1
    highest_score = 0
    for (i, j), height in np.ndenumerate(input_arr):
        if i> 0 and j>0 and i<xmax and j<ymax:
            right_score = 0
            left_score=0
            up_score=0
            down_score =0
            tree_score = 0

            for x in range(j+1,ymax+1):
                right_score+=1
                if input_arr[i,x] >= input_arr[i,j]:
                    break   
            for x in range(j-1,-1, -1):
                left_score+=1
                if input_arr[i,x] >= input_arr[i,j]:
                    break
            for x in range(i+1,xmax+1):
                down_score+=1
                if input_arr[x,j] >= input_arr[i,j]:
                    break
            for x in range(i-1,-1, -1):
                up_score+=1
                if input_arr[x,j] >= input_arr[i,j]:
                    break

            tree_score = right_score*left_score*up_score*down_score
            if tree_score>highest_score:
                highest_score = tree_score
    return highest_score
            
def process_answers():
    with open('day8.txt') as f:
        ls = []
        for line in f:
            ls.append(list(map(int,list(line.strip()))))

    # Read into an array and initialise height array
    arr = np.array(ls, dtype=np.int)
    height_arr =np.zeros((arr.shape[0],arr.shape[1]))

    height_arr = set_visible_trees(arr,height_arr, 'h', False)
    height_arr = set_visible_trees(arr,height_arr, 'h', True)
    height_arr = set_visible_trees(arr.T,height_arr, 'v', False)
    height_arr = set_visible_trees(arr.T,height_arr, 'v', True)

    print("The answer to part 1 is ",height_arr.sum()) #1560
    print("The answer to part 2 is ",get_scenic_score(arr)) #1560
    return

process_answers()
