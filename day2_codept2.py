
with open('day2.txt') as f:

    score = 0
    for line in f:
        test = line.split()
        opponent = test[0]
        mine = test[1]

        if mine == 'X':
            if opponent == 'A':
                score+=3
            elif opponent == 'B':
                score+=1
            elif opponent == 'C':
                score+=2

        elif mine == 'Y':
            score+=3
            if opponent == 'A':
                score+=1
            elif opponent == 'B':
                score+=2
            elif opponent == 'C':
                score+=3

        elif mine == 'Z':
            score+=6
            if opponent == 'A':
                score+=2
            elif opponent == 'B':
                score+=3
            elif opponent == 'C':
                score+=1

print(score)
