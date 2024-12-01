# read in file
def create_elf_dict(filename):
    """
    Read in the file. Create the elf position dictionary
    """
    with open(filename, encoding='UTF8') as file:
        state = []
        wall= set()
        up = set()
        right = set()
        down = set()
        left = set()
        line_num = 0
        width = 0

        for line in file:
            line_num +=1
            line = line.replace('\n','')

            for pos, element in enumerate (line):
                pos+=1
                if element == '#':
                    wall.add((pos,line_num))
                elif element  == '>':
                    right.add((pos,line_num))
                elif element  == 'v':
                    down.add((pos,line_num))                
                elif element  == '<':
                    left.add((pos,line_num))                
                elif element  == '^':
                    up.add((pos,line_num))
                if pos> width:
                    width = pos

    return elf_dict