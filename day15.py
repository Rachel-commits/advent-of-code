
from collections import defaultdict 
import re
from datetime import datetime


def update_signal_dict (signal_dict, sx,sy,bx,by):

    #Calculate Manhattan Distance
    distance = abs(sx-bx) + abs(sy-by)
    signal_dict[(sx,sy)] = distance

    return signal_dict

def mark_clear_path(s_x,s_y,dist, row_positions, row_num):

    #get the difference between the signal y coord and 
    #row num in order to determine the xmin and xmax check values
    # This reduces the amount of checing needed in the loop function
    ydiff=  abs(s_y - row_num)
    x_check = (dist - ydiff)
    xmin = s_x - x_check 
    xmax = s_x + x_check

    # Append to list if row coord is between the min and the max point
    if x_check >=0:
        for i in range(xmin,xmax +1 ):
            row_positions.add(i) 
    return row_positions


def calculate_number_positions(row_num, signal_dict, beacon_dict):

    row_positions = set()

    for (x, y), distance in signal_dict.items():
        # For each signal calulate the positions on given row where 
        # a beacon cannot exits 
        row_positions = mark_clear_path(x, y, distance, row_positions, row_num)

    row_positions
    # Get all known beacon positions in that row  
    beacon_set = set(beacon_dict[row_num]) #
    # return number of clear positions excluding beacons
    return len(row_positions-beacon_set)

def check_size_append( x,y,edge_list,max_coord):
    if x<0 or x>max_coord or y<0 or y>max_coord:
        return edge_list
    else:
        return edge_list.append((x,y))


# Part 2 Function
def get_edges(signal_dict, max_coord):

    count=0
    edge_list =[]
    for (x, y), distance in signal_dict.items(): 
      
        i = 0
        distance +=1
        # Append 4 edge coordinates for each iteration (1st and last
        # iteration only append 2)
        for i in range(distance):

            # On the first round
            check_size_append(x+distance-i,y+i,edge_list,max_coord)
            check_size_append(x-distance+i,y+i,edge_list,max_coord)

            if i>0:
                check_size_append(x+distance-i,y-i,edge_list,max_coord)
                check_size_append(x-distance+i,y-i,edge_list,max_coord)

        # On the last round
        i+=1
        check_size_append(x+distance-i,y+i,edge_list,max_coord)
        check_size_append(x-distance+i,y-i,edge_list,max_coord)

        count+=1
        print("signal", count,(x,y), " complete",len(edge_list),datetime.now())
        
    return edge_list

# Part 2 Function
def check_seen(edge_list,signal_dict):
    print("running check_seen")
    count = 1
    
    # edge_list = list(edge_list)
    # For each edge coordinate 
    for coord in edge_list:
        found = False
        xcoord = coord[0]
        ycoord =coord[1]
        # Check against every signal. If  seen then break out function
        for (sx, sy), dist in signal_dict.items(): 
            if abs(sx-xcoord) + abs(sy-ycoord) <=dist:
                found = True
                break
            else:
                continue
        #If not seen by any of the signal then calc ansr and retun the coord
        if found == False:
            return coord, 4000000*xcoord + ycoord
        
        count+=1
        if count%1000000 ==0:
            print("The counter is ",count, datetime.now() )
    return (0,0), 0

def process_file(filename):

    signal_dict ={}
    beacon_dict =defaultdict(list)         
    with open (filename) as file:
        # Read in file line by line and append to signla nad beacon dict
        for line in file:
            line = line.strip('\n') +'aaa'
            line_list = line.split(':')
            sensor = line.split(':')[0] +'aaa'
            beacon = line.split(':')[1]
            s_x= int(re.search('Sensor at x=(.+?), y=', sensor).group(1))
            s_y= int(re.search('y=(.+?)aaa', sensor).group(1))
            b_x= int(re.search('beacon is at x=(.+?), y=', beacon).group(1))
            b_y= int(re.search(', y=(.+?)aaa', beacon).group(1))

            signal_dict = update_signal_dict(signal_dict, s_x,s_y,b_x,b_y)
            beacon_dict[b_y].append(b_x)

    return signal_dict, beacon_dict



#4883971
#Part 1 
def run_puzzle():

    # Create the dictionaries
    signal_dict, beacon_dict = process_file('day15.txt')
    # calculate the number of positions for part 1 
    num_positions = calculate_number_positions(2000000, signal_dict, beacon_dict)
    print("The number of clear position is ", num_positions)

    #Part 2 
    #Calcualte all the edges for the signals
    edge_list = get_edges(signal_dict, 4000000)
    
    # Now for all the edges check if they can be seen by any signal
    # If not then thats the answer
    coord, answer = check_seen(edge_list,signal_dict) 
    print("The answer is ", answer, " at this coord ", coord)    

run_puzzle()
