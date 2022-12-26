"""
Advent of Code 2022
Day 23: Full of hot air
Find the snafu representation total.
https://adventofcode.com/2022/day/25
"""
def process_file(filename):
    """
    Read in file convert to decimal and total up
    """
    total = 0
    with open(filename, encoding='UTF8') as file:
        for line in file:
            decimal = 0
            line = line.replace('\n','')
            line = list(line)
            line = ['-1' if item == "-" else item for item in line]
            line = ['-2' if item == "=" else item for item in line]
            snafu = list(map(int,line))
            snafu.reverse()

            for i, number in enumerate(snafu):
                decimal += number*pow(5,i)
            total += decimal
    return total

def get_five_power(number):
    """
    Given a number find the maximum
    power of 5 less than the number
    """

    five_power = 0
    i = -1
    while five_power < number:
        i +=1
        five_power = pow(5,i)
    return i - 1


def convert_to_snafu(number):
    """
    Given a decimal number convert to
    snafu representation
    """
    decimal_list = []
    # find the start index
    start_index = get_five_power(number)

    while start_index >= 0:
        div , mod = divmod(number,  pow(5,start_index))
        decimal_list.append(div)
        start_index -=1
        number = mod

    # reverse to make it easier
    decimal_list.reverse()
    list_length = len(decimal_list)

    #Now we iterate through the list in order to replace numbers > 3
    for i in range(list_length):
        if decimal_list[i] <= 2:
            continue
        else:
            # we need to increment the next position by 1 and take 5 from the current position
            decimal_list[i] = decimal_list[i] - 5
            if i+1 == list_length:
                decimal_list.append(1)
            else:
                decimal_list[i+1] = decimal_list[i+1] + 1

    #reverse the list back
    decimal_list.reverse()
    # convert to a string
    decimal_list = list(map(str,decimal_list))
    decimal_list = ['-' if item == "-1" else item for item in decimal_list]
    decimal_list = ['=' if item == "-2" else item for item in decimal_list]
    decimal_string = ''.join(decimal_list)

    return decimal_string


def solve_puzzle():
    """
    Function to run the code to import
    the file and solve the puzzle
    """
    total = process_file(r'data\day25.txt')
    snafu = convert_to_snafu(total)
    print("The answer to part 1 is ", snafu)

solve_puzzle()
