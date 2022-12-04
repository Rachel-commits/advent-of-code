

with open('day1.txt') as f:
    
    calories = 0
    elf = 1
    highest_elf = 1 
    highest_calories = 0

    for line in f:
        line = line.rstrip('\n')
        if line == '':
            if calories > highest_calories:
                highest_calories = calories
                highest_elf = elf
            elf+=1
            calories =0
        else:
            calories+= int(line)

print(highest_elf, highest_calories)