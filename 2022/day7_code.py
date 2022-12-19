

from collections import defaultdict
                 
with open('day7.txt') as f:

    file_sum = 0
    dict_dir_size ={}
    directory_path =[]
    used_space=0
    total = 0

    for line in f:
        line = line.strip('\n')
        # set current directory
        if line[0:4] =='$ cd':
            dir = line[5:]

            if dir =='..':
                directory_path.pop(-1)

            elif dir !='':
                directory_path.append(dir)
                full_name = '/'.join(directory_path)
                dict_dir_size[full_name]=0
       # No action  for ls 
        elif line[0:4] =='$ ls':
            continue

        # No action for dir 
        elif line[0:3] =='dir':
            continue
        
        #get the contained files
        else:
            file_size = int(line.split()[0])
            file_sum += file_size
            full_name = '/'.join(directory_path)
            dict_dir_size[full_name]+=file_size

            directory_path_temp = directory_path.copy()

            #uncomment this for part 1
            while len(directory_path_temp)>1:
                directory_path_temp.pop(-1)
                full_name = '/'.join(directory_path_temp)
                dict_dir_size[full_name]+=file_size

#part1
for x in dict_dir_size:
    if dict_dir_size[x]<=100000:
        total+=dict_dir_size[x]
print("The sum of dir <100000 is ",total)

#part2
unused_space = 70000000 - file_sum
space_needed = 30000000 - unused_space

sorted_dict = dict(sorted(dict_dir_size.items(), key=lambda item: item[1]))

for x in sorted_dict:
    if sorted_dict[x]>=space_needed:
        print("The directory to delete is ",x, "and will free up " , sorted_dict[x])
        break
