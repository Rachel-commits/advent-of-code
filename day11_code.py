
from datetime import datetime
monkey_dict = {}


class Monkey:

    monkey_number=-1
    starting_items=[]
    operation_sign =''
    operation_number =''
    divisible_by =-1
    true_monkey = -1
    false_monkey  =-1
    inspected_count = 0
    throw_dict ={}
  
    # parameterized constructor
    def __init__(self,monkey_number , input_string):
        self.monkey_number = monkey_number
        self.input_string = input_string
        self.parse_input(input_string)

    def parse_input(self,input_string):
        input_string = input_string.split('\n')

        self.starting_items = list(map(int,input_string[0].split(':')[1].split(',')))

        self.operation_sign = input_string[1].split('=')[1].split(' ')[2]
        self.operation_number = input_string[1].split('=')[1].split(' ')[3]

        self.divisible_by = int(input_string[2].split(':')[1].split(' ')[3]) 
        
        self.true_monkey = int(input_string[3][-1])
        self.false_monkey = int(input_string[4][-1])

    def inspect_item(self,current_worry, scalar):
  
        self.inspected_count +=1
        if self.operation_number =='old':
            op_num = current_worry
        else:
            op_num = int(self.operation_number)
        
        if self.operation_sign == '+':
            current_worry +=op_num 
        elif self.operation_sign == '-':
            current_worry -= op_num 
        elif self.operation_sign == '*':
            current_worry *= op_num 
        elif self.operation_sign == '/':
            current_worry /= op_num 

        if scalar ==1:
            current_worry = current_worry//3
        else:
            remainder = current_worry % scalar
            current_worry = scalar + remainder

        return current_worry
     
    def throw_items (self, scalar):
        true_list = []
        false_list = []
        self.throw_dict={}
        for item in self.starting_items:
            current_worry = self.inspect_item(item, scalar)
            if current_worry % self.divisible_by ==0:
                true_list.append(current_worry)
            else:
                false_list.append(current_worry)
        if len(true_list) >0:
            self.throw_dict[self.true_monkey] = true_list
        if len(false_list) >0:
            self.throw_dict[self.false_monkey] = false_list
        self.starting_items=[]
        return self.throw_dict
    
    def catch_items(self, item_list):
        for item in item_list:
            self.starting_items.append(item)

def create_monkeys():      
    with open("day11.txt") as f:
        for line in f:
            if line[0:6]== 'Monkey':
                monkey_number = int(line[7])
                monkey_info = ''
            else:
                monkey_info +=line
            if line == '\n':
                monkey = Monkey(monkey_number,monkey_info)
                monkey_dict[monkey_number] = monkey
        # Add the last monkey
        monkey = Monkey(monkey_number,monkey_info)
        monkey_dict[monkey_number] = monkey
    return monkey_dict


def generate_rounds(num_rounds, monkey_dict,scalar):
    for round in range(num_rounds):
        for throwers in monkey_dict:
            #throw item
            lookup_dict = monkey_dict[throwers].throw_items(scalar)
            #update other monkeys
            for catchers in lookup_dict:
                monkey_dict[catchers].catch_items( lookup_dict[catchers])
    return monkey_dict

def  calc_top_2(monkey_dict):
    inspect_dict ={}
    for monkey_num in monkey_dict:
        inspect_dict[monkey_num] = monkey_dict[monkey_num].inspected_count

    top2_monkeys = sorted(inspect_dict, key=inspect_dict.get, reverse=True)[:2]
    answer = inspect_dict[top2_monkeys[0]] * inspect_dict[top2_monkeys[1]]
    return answer

def get_test_scalars():
    scalar = 1
    for monkey_num in monkey_dict:
        scalar *=monkey_dict[monkey_num].divisible_by
    return scalar



# part 1 
monkey_dict = create_monkeys()
monkey_dict = generate_rounds(20, monkey_dict, 1)
answer = calc_top_2(monkey_dict)
print("The answer to part 1 is ", answer)

# part 2
monkey_dict = create_monkeys()
scalar = get_test_scalars()
monkey_dict = generate_rounds(10000, monkey_dict, scalar)
answer = calc_top_2(monkey_dict)
print("The answer to part 2 is ", answer)

