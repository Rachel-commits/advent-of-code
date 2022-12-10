
# R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2

import numpy as np
from collections import defaultdict


hpos =[0,0]
tpos =[0,0]
tail_visits=[]
coords=(tpos[0],tpos[1])
tail_visits.append(coords)

rope_dict = defaultdict(list)
for i in range(10):
    rope_dict[i].append([0,0])

def move_rope(rope_number,head_list,tail_list, tail_visits):
    relative_tail = [0,0]
    relative_tail[0] = head_list[0] - tail_list[0] 
    relative_tail[1] = head_list[1] - tail_list[1]
    x_increment = np.sign(relative_tail[0])
    y_increment = np.sign(relative_tail[1])  
 
    # move horizontal
    if abs(relative_tail[0]) >1  and abs(relative_tail[1]) == 0:
        tail_list[0] += x_increment
    
    #move vertical
    elif abs(relative_tail[1]) >1 and abs(relative_tail[0]) == 0:
        tail_list[1] += y_increment
    
        #move diagonal
    elif abs(relative_tail[0]) >1 or abs(relative_tail[1]) >1:
        tail_list[0] += x_increment
        tail_list[1] += y_increment
 
    if rope_number ==8:
        coords=(tail_list[0],tail_list[1])
        tail_visits.append(coords)
    return head_list, tail_list,tail_visits
 
def move_all_ropes(head_list,tail_visits):
    for i in range(9):

        if i ==0:
            first_list = head_list.copy()
            follow_list = rope_dict[1][0]

        elif i>0:
            first_list = rope_dict[i][0]
            follow_list = rope_dict[i+1][0]
        
        first_list,follow_list, tail_visits = move_rope(i,first_list,follow_list, tail_visits)
        rope_dict[i].append(first_list)
        rope_dict[i+1].append(follow_list)

    return tail_visits

def move_head_and_tail(head_list,tail_visits,direction, length):
    if direction in ('R', 'U'):
        step = 1
    else:
        step=-1
    
    if direction in ('L','R'):
        for i in range(length+1):
            if i>0:
                head_list[0]+=step
                tail_visits = move_all_ropes(head_list,tail_visits)
                


    elif direction in ('U','D'):
        for i in range(length+1):
            if i>0:
                head_list[1]+=step
                tail_visits = move_all_ropes(head_list,tail_visits)
    return head_list, tail_visits

i=0
with open('day9.txt') as f:
    ls = []
    for line in f:
        i+=1
        line = line.strip('\n')
        line = line.split(' ')
        direction = line[0]
        length = int(line[1])
        hpos, tail_visits = move_head_and_tail(hpos,tail_visits,direction,length)
        
        # print(i,line, len(set(tail_visits)), tpos)
        # print('xxxxxxxxxxxxxx')
        # print(hpos)
        # print(tpos)
        # print(tail_visits)
        # print(len(set(tail_visits)))

print("The number of positions is ", len(set(tail_visits)))