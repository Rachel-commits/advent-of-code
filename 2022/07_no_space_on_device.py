"""used_space
Advent of Code 2022
Day 7: No Space left on device
Find the sum of the space freed up when
deleting directories
https://adventofcode.com/2022/day/7
"""

def create_direct_size_dict(filename):
    """
    Read in file and create directory size dictionary
    """
    with open(filename, encoding='UTF8') as file:

        file_sum = 0
        dict_dir_size ={}
        directory_path =[]

        for line in file:
            line = line.strip('\n')
            # if command is `cd` set current directory
            if line[0:4] =='$ cd':
                directory = line[5:]

                if directory =='..':
                    directory_path.pop(-1)
                elif directory !='':
                    directory_path.append(directory)
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

                #For each directory in path  add the file size
                while len(directory_path_temp)>1:
                    directory_path_temp.pop(-1)
                    full_name = '/'.join(directory_path_temp)
                    dict_dir_size[full_name]+=file_size

    return dict_dir_size, file_sum

def calc_part1(dict_dir_size):
    """
    Find all directories less than 100000 in size
    and calculate thei total size
    """
    total = 0
    for directory in dict_dir_size:
        if dict_dir_size[directory]<=100000:
            total+=dict_dir_size[directory]
    print("The sum of dir <100000 is ",total)

def calc_part2(dict_dir_size, file_sum):
    """
    Find the smallest directory to delete to free up enough
    space.
    """
    unused_space = 70000000 - file_sum
    space_needed = 30000000 - unused_space

    sorted_dict = dict(sorted(dict_dir_size.items(), key=lambda item: item[1]))

    for directory in sorted_dict:
        if sorted_dict[directory]>=space_needed:
            print("The directory to delete is ", directory,
             "and will free up " , sorted_dict[directory])
            break

def run_puzzle():
    """
    Read in file and calculate part 1 and 2.
    """
    dict_dir_size, file_sum = create_direct_size_dict(r'data\day7.txt')
    calc_part1(dict_dir_size)
    calc_part2(dict_dir_size, file_sum)


run_puzzle()
