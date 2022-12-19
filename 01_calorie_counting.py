'''Day 1: Calorie Counting - Calculating the elves with the most calories'''
def process_file(filename):
    '''Loops through input file and creates a
    dictionary with the total calories for each elf'''
    with open(filename, encoding="utf8") as file:

        calories = 0
        elf = 1
        elf_dict={}

        for line in file:
            line = line.rstrip('\n')
            if line == '':
                elf_dict[elf] = calories
                elf +=1
                calories =0
            else:
                calories+= int(line)
    return elf_dict

def get_total_calories(filename, num_of_elves):
    '''calaulate the total calories for the top n elves'''
    total_calories = 0
    elf_dict = process_file(filename)
    highest_elf = sorted(elf_dict, key=elf_dict.get, reverse=True)[:num_of_elves]

    for elf in highest_elf:
        total_calories += elf_dict[elf]

    print ("The total number calories carried by the top "
    , num_of_elves, " elf is ", total_calories)

#Part 1
get_total_calories(r'data\day1.txt',1)
# Part2
get_total_calories(r'data\day1.txt',3)
