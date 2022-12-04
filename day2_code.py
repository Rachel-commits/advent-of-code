
with open('day2.txt') as f:
    
    score = 0

    for line in f:
        test = line.split()
        opponent = test[0]
        mine = test[1]
        # points for selection
        if mine == 'X':
            score+=1
            if opponent == 'A':
                score+=3
            elif opponent == 'C':
                score+=6

        elif mine == 'Y':
            score+=2
            if opponent == 'B':
                score+=3
            elif opponent == 'A':
                score+=6

        elif mine == 'Z':
            score+=3
            if opponent == 'C':
                score+=3
            elif opponent == 'B':
                score+=6

print(score)
