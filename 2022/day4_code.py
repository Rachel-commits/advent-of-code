
def count_overlap(type):
    count=0
    with open('day4.txt','r') as file:
        for line in file:
            elf1, elf2 = line.strip().split(',')
            sections1 = generate_sections(elf1)
            sections2 = generate_sections(elf2)
            if type == 'all':
                if all_overlap(sections1,sections2):
                    count +=1
            elif type == 'any':
                if any_overlap(sections1,sections2):
                    count +=1
    return count
       
def generate_sections(elf):
    start, end = elf.split('-')
    return list(range(int(start), int(end)+1))

def all_overlap(list1, list2): 
    if all(item in list1 for item in list2):
        return True
    elif all(item in list2 for item in list1):
        return True 
    else: 
        return False

def any_overlap (list1, list2):
    if any(item in list1 for item in list2):
        return True
    else: 
        return False


#part1 
print("The number of sections overlapping is ", count_overlap('all'))

#part2 
print("The number of sections overlapping is ", count_overlap('any'))

