"""
Advent of Code 2024
Day 5: Print Queue
Part 1:

The first section specifies the page ordering rules, one per line.
The first rule, 47|53, means that if an update includes both page
number 47 and page number 53, then page number 47 must be printed
at some point before page number 53. (47 doesn't necessarily need
to be immediately before 53; other pages are allowed to be between
them.)

The second section specifies the page numbers of each update. Because
most safety manuals are different, the pages needed in the updates are
different too. The first update, 75,47,61,53,29, means that the update
consists of page numbers 75, 47, 61, 53, and 29.

To get the printers going as soon as possible, start by identifying which
updates are already in the right order.

For some reason, the Elves also need to know the middle page number of each
update being printed. Because you are currently only printing the correctly
ordered updates, you will need to find the middle page number of each
correctly-ordered update.

Part 2:
While the Elves get to work printing the correctly-ordered updates, you have
a little time to fix the rest of them.

For each of the incorrectly-ordered updates, use the page ordering rules to
put the page numbers in the right order. For the above example, here are the
three incorrectly-ordered updates and their correct orderings:
After taking only the incorrectly-ordered updates and ordering them correctly,
their middle page numbers are 47, 29, and 47. Adding these together produces 123.
Find the updates which are not in the correct order. What do you get if you add
up the middle page numbers after correctly ordering just those updates?

https://adventofcode.com/2024/day/5
"""

def get_input(filename)-> tuple[list,list]:

    with open(filename, 'r') as file:
        lines = file.read().splitlines()
    
    rule_list = []
    printing_list= []
    
    for line in lines:
        # Check if the line contains '|' or ','
        if '|' in line:
            pair = list(map(int, line.split('|')))
            rule_list.append(pair)
        elif ',' in line:
            pages = list(map(int, line.split(',')))
            printing_list.append(pages)
    
    return rule_list, printing_list

def solve_puzzle(rules_list: list, pages_list: list, part2: bool) -> int:

    rule_passed = False
    middle_page_sum = 0

    for update in pages_list:
        reordered = False
        rule_index = 0

        while rule_index < len(rules_list):
            rule = rules_list[rule_index]
            try:
                before_index = update.index(rule[0])
                after_index = update.index(rule[1])
                if before_index < after_index:
                    rule_passed = True
                else:
                    rule_passed = False
                    if not part2:
                        break # exit early for part 1
                    else: # for part 2 reorder the list
                        reordered = True
                        update[before_index] = rule[1]
                        update[after_index] = rule[0]
                        rule_index = 0
                        continue

            except ValueError: # page from rule will not always exist in the update
                pass

            rule_index+=1

        if (rule_passed and not part2) or (part2 and reordered):
            middle_page_sum += update[int((len(update)-1)/2)]

    return middle_page_sum


def main() -> None:
    rule_list, pages_list = get_input('2024/data/day5.txt')

    part1_result = solve_puzzle(rule_list, pages_list, part2=False)
    part2_result = solve_puzzle(rule_list, pages_list, part2=True)

    print(f"The answer to part 1 is: {part1_result}")
    print(f"The answer to part 2 is: {part2_result}")

if __name__ == '__main__':
    main()