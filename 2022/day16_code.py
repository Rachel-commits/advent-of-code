
from collections import defaultdict 
import re

def process_input(filename):
    flow_rate_dict = {}
    tunnel_dict = {}
    with open(filename) as f:
        for line in f:
            line = line.strip('\n') 
            valve_instr = line.split(';')[0]
            tunnel_instr  = line.split(';')[1].replace (',','').split()
            valve= re.search('Valve (.+?) has', valve_instr).group(1)
            rate= int(valve_instr.split('=')[1])
            # test = len(tunnel_instr)
            tunnels = tunnel_instr[4:]
            
            # create dicts
            flow_rate_dict[valve] = rate
            tunnel_dict[valve] = tunnels
    return flow_rate_dict, tunnel_dict

## create a graph_dict of all the possible routes to non zero valves
def generate_pairs(flow_rate_dict):
    pair_list =[]
    for end_valve, flow_rate in flow_rate_dict.items():
        if end_valve !='AA':
            pair_list.append(('AA' ,end_valve))
        if flow_rate > 0:
            for valve, rate in flow_rate_dict.items():
                if valve != 'AA':
                    if valve != end_valve:
                        pair_list.append((valve ,end_valve))   
    return pair_list 

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

def create_pair_dict():
    flow_rate_dict, tunnel_dict = process_input('data\day16ex.txt')
    pairwise_list = generate_pairs(flow_rate_dict)

    pair_dict ={}
    for pair in pairwise_list:
        shortest=  get_shortest_path(tunnel_dict, pair[0],pair[1])
        pair_dict[pair] =len(shortest)-1

    #Pair dict has paur as they key and then the disance
    # print(pair_dict )
    return flow_rate_dict, pair_dict

def dfs(pair_dict,start, neighbours):
 

    time = 30
    visited = []
    neighbours = []
    for valve, val in flow_rate_dict.items():
        if val > 0:
            neighbours.append(valve)
    # keep track of nodes to be checked
    queue = [([start], 30, 0,)]



    while queue:
        # get the last path from the queue
        state = queue.pop()
        # get the last node from the path
        path = state[0]
        node = path[-1]
        time = state[1]
        pressure = state[2]
        # open = state[3]

        if time>0:
            #  new_path = list(path)
      
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                if neighbour not in path and time >=0:
  
                    temp_time = time -pair_dict[(node, neighbour)] -1
                   

                    if time >=0:
                        path.append(neighbour)
                        time = temp_time
                        pressure = (time)*flow_rate_dict[neighbour] + pressure
                        
                  
                    

            queue.append((path, time, pressure))
            queue_copy = queue.copy()
                  

            # Add the node to the visited list
            visited.append(node)
        if len(queue) % 1000  ==0:
            print(len(queue)) 
            print(time, pressure)
    return queue_copy


# def bfs(pair_dict,start, neighbours):
 

#     time = 30
#     visited = []
#     neighbours = []
#     for valve, val in flow_rate_dict.items():
#         if val > 0:
#             neighbours.append(valve)
#     # keep track of nodes to be checked
#     queue = [([start], 30, 0)]



#     while queue:
#         # get the first path from the queue
#         state = queue.pop(0)
#         # get the last node from the path
#         path = state[0]
#         node = path[-1]
#         time = state[1]
#         pressure = state[2]
#         if time>0:
      
#             # go through all neighbour nodes, construct a new path and
#             # push it into the queue
#             for neighbour in neighbours:
#                 if neighbour not in path:


#                     new_path = list(path)
#                     new_path.append(neighbour)
#                     new_time = time -pair_dict[(node, neighbour)] -1
#                     new_pressure = (new_time)*flow_rate_dict[neighbour] + pressure
#                     queue.append((new_path, new_time, new_pressure))
#                     queue_copy = queue.copy()

                  

#             # Add the node to the visited list
#             visited.append(node)
#         if len(queue) % 1000  ==0:
#             print(len(queue)) 
#             print(time, pressure)
#     return queue_copy

# def dfs_traversal(input_graph, source):
#     stack = list()
#     visited_list = list()
#     stack.append(source)
#     visited_list.append(source)
#     while stack:
#         vertex = stack.pop()
#         print(vertex, end=" ")
#         for u in input_graph[vertex]:
#             if u not in visited_list:
#                 stack.append(u)
#                 visited_list.append(u)

flow_rate_dict, pair_dict = create_pair_dict()

possible_paths = dfs(pair_dict, 'AA', flow_rate_dict)
print(possible_paths)

pressure = 0
max = ()
for i in possible_paths:
    if i[2]>pressure and i[1]>=0:
        pressure = i[2]
        max = i
# print(possible_paths)
print(max)

# print("DFS traversal of graph w'AAith source A is:")
# dfs_traversal(tunnel_dict,'AA' )
