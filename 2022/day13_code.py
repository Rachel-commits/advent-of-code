import ast
import functools

def get_comparison_type(pair1, pair2):

    # Both ints - compare directly
    if type(pair1) == int and type(pair2) == int:
        #return -1 for correct 1 for incorrect and 0 for same
        if pair1 < pair2:
            return -1
        elif pair1 > pair2:
            return 1
        else:
            return 0

    # If mixed types then convert the int to a list
    elif type(pair1) == int:
        pair1 = [pair1]
    elif type(pair2) == int:
        pair2 = [pair2]

    # if list 1 is empty and list 2 is not then its in the right order
    # if list 2 runs out before list 1 then not in the right order
    if len(pair1) == 0 and len(pair2) == 0:
        return 0
    elif len(pair1) == 0:
        return -1
    elif len(pair2) == 0:
        return 1

    # loop through elemets in the first list until a non same comparison is found 
    for j, element1 in enumerate(pair1):

        # if list 2 runs out then return incorrect 
        if (j == len(pair2)):
            return 1

        element2 = pair2[j]  
        # call the function recursively to compare the 2 elements
        # if they are not the same then return the result
        check = get_comparison_type(element1,element2)
        if check in (-1,1):
            return check

    # if list 1 runs out then its in the correct order  
    if len(pair1) < len(pair2):
        return -1
    
    return 0
    
def process_input(filename):
    with open("day13.txt") as file:
        index_sum=0
        line_num = 0
        pair_index = 1
        pair1 =[]
        pair2 =[]
        pairs=[]

        for line in file:
            line = line.strip('\n')
            line_num += 1

            # Read in the first and secon d line then compare the 2 lists
            if (line_num+3)%3 == 1:
                pair1 = ast.literal_eval(line) 
                pairs.append(pair1)      
            elif (line_num+3)%3 == 2:
                pair2 = ast.literal_eval(line)
                pairs.append(pair2)         
            else:
                if get_comparison_type(pair1,pair2) ==-1:
                    index_sum += pair_index
                pair_index +=1

    return index_sum, pairs
        
def get_decoder_key(pair_list):

    # Add the additional divider packets
    pair_list.append([[2]])
    pair_list.append(([[6]]))

    #sort the list according to the comparison function
    pairssorted = sorted(pair_list, key=functools.cmp_to_key(get_comparison_type))
    # decoder kes is the index of divider 2 and 6
    decoder_key = 1
    for i, p in enumerate(pairssorted):
        if (p == [[2]]) or (p == [[6]]):
            decoder_key *= (i+1)
    return decoder_key


#Part 1 
index_sum, pairs = process_input('day13.txt')
print ("The sum of the indices where the pairs are in the correct order is ", index_sum)

#Part 2 
decoder_key = get_decoder_key(pairs)
print ("The value of the decoder key is ", decoder_key)
