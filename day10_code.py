
execution = {}

def create_execution_dict(filename):
    cycle = 0
    with open(filename) as f:
        ls = []
        for line in f:

            line = line.strip('\n')
            line = line.split(' ')

            if line[0] == 'addx':
                cycle +=2
                execution[cycle] = int(line[1])
            else:
                cycle +=1

def calc_signal_strength(cycle):
    score =1
    i=0
    for i in range(cycle):
        score += execution.get(i,0)
    signal_strength = score*cycle
    return signal_strength

def add_strengths(start,stop,step):
    total_signal_strength=0
    for cycle in range(start,stop,step):
        signal_strength = calc_signal_strength(cycle)
        total_signal_strength +=signal_strength
    return total_signal_strength

def get_pixels():
    draw =[]
    i=0
    for i in range(max(execution)):
        if  i ==0:
            posn = 1 
        if i%40 <= posn+1 and i%40>= posn-1:
            draw.append(i)
        posn += execution.get(i+1,0)
    return draw

def generate_output(input_list):
    line_output =""
    final_output=""
    i=0
    for i in range(max(execution)+1):
        if (i in input_list):
            line_output+="#"
        else:
            line_output+="."
        if (i+1)%40 ==0:
            final_output+=line_output+'\n'
            line_output = ""
    return final_output

# Part 1 
create_execution_dict('day10.txt')
total_signal_strength = add_strengths(20,241,40)
print("The total signal strength is ", total_signal_strength)

# Part 2 
create_execution_dict('day10.txt')
draw_list = get_pixels()
print(generate_output(draw_list))

