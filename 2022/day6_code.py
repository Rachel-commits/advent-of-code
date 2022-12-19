def read_file(filename):
    with open (filename) as f:
        return list(f.read())


def get_start_position(input_list, num_chars):
    check_list =[]
    for i, char in enumerate(input_list):
        if i < num_chars:
            check_list.append(char)
        else:
             #  check  for dupes
            if(len(set(check_list)) <  len(check_list)):
                check_list.pop(0)
                check_list.append(char)
            else:
                break
    return i

def run_puzzle():
    input = read_file('day6.txt')
    pos1 = get_start_position(input,4)
    pos2 = get_start_position(input,14)
    print("The answer to part 1 is ", pos1)
    print("The answer to part 2 is ", pos2)
    return

run_puzzle()
