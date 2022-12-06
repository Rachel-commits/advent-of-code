with open('day1.txt') as f:
    
    calories = 0
    elf = 1
    first_elf = 1 
    second_elf =1
    third_elf = 1
    highest_calories1 = 0
    highest_calories2 = 0
    highest_calories3 = 0


    for line in f:
        line = line.rstrip('\n')
        if line == '':
            if calories> highest_calories1:
                highest_calories3 = highest_calories2
                highest_calories2 = highest_calories1
                highest_calories1 = calories
                third_elf = second_elf
                second_elf = first_elf
                first_elf = elf

            elif calories> highest_calories2:
                highest_calories3 = highest_calories2
                highest_calories2 = calories
                third_elf = second_elf
                second_elf = elf
            
            elif calories> highest_calories3:
                highest_calories3 = calories
                third_elf = elf

            elf+=1
            calories =0
        else:
            calories+= int(line)

total_calories = highest_calories1 + highest_calories2 + highest_calories3

print(total_calories)

