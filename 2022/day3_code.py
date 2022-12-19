

from string import ascii_uppercase, ascii_lowercase
priority = 0
alphabet = {v:k+1 for k,v in enumerate(ascii_lowercase + ascii_uppercase)}
 
def get_priority(rucksack):
    #split compartments
    position = int(len(rucksack)/2)
    section1, section2 = rucksack[:position], rucksack[position:]
    #find common items
    shared_items = ''.join([
        item for item in section1
        if item in section2
    ])
    return alphabet.get(shared_items[0])

def get_badge(bag1,bag2,bag3):

    shared_items1 = ''.join([
        item for item in bag1
        if item in bag2
    ])

    shared_items2 = ''.join([
        item for item in shared_items1
        if item in bag3
    ])
    return alphabet.get(shared_items2[0])
    
    

#part 1 
with open('day3.txt') as f:
    for rucksack in f:
        priority += get_priority(rucksack.rstrip('\n'))
        
print(priority)

#part 2
line_num = 1
priority = 0
with open('day3.txt') as f:
    for rucksack in f:
        if line_num %3 ==1:
            rucksack1= rucksack.rstrip('\n')
        elif line_num %3 ==2:
            rucksack2= rucksack.rstrip('\n')
        elif line_num %3 ==0:
            rucksack3= rucksack.rstrip('\n')
            priority +=get_badge(rucksack1,rucksack2,rucksack3)
        line_num += 1
    print("Part2 priority score is: ",priority)



