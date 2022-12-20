from typing import List


def get_stack_list(all_data):
    stack_list = []
    for line in all_data:
        if line == '':
            break
        stack_list.append(line)
    return stack_list


def get_instruction_list(all_data, starting_line):
    instruction_list = []
    current_line = 0
    for line in all_data:
        current_line += 1
        if current_line > starting_line + 1:
            instruction_list.append(line)
    return instruction_list


def get_starting_stacks(stack_list):
    # convert string to list
    # get the longest line and pad all lines
    longest_line = 0
    for line in stack_list:
        longest_line = max(longest_line, len(line))
    # pad all the lines
    new_stack_list = []
    for line in stack_list:
        new_stack_list.append(line.ljust(longest_line))
    rotated_list = list(zip(*new_stack_list[::-1]))
    print(rotated_list)
    starting_stack = []
    for line in rotated_list:
        line_list: List = list(line)
        if line_list[0].isdigit():
            a_stack = []
            line_list.pop(0)
            for item in line_list:
                if item.isupper():
                    a_stack.append(item)
            starting_stack.append(a_stack)
    return starting_stack


def update_stack(stacks, instruction_string):
    # move 1 from 2 to 1
    _, num_items, _, from_stack_number, _, to_stack_number = instruction_string.split()
    num_items = int(num_items)
    from_stack_index = int(from_stack_number) - 1
    to_stack_index = int(to_stack_number) - 1
    from_stack = stacks[from_stack_index]
    to_stack = stacks[to_stack_index]
    for item_num in range(num_items):
        to_stack.append(from_stack.pop())


def update_queue(stacks, instruction_string):
    # move 1 from 2 to 1
    _, num_items, _, from_stack_number, _, to_stack_number = instruction_string.split()
    num_items = int(num_items)
    from_stack_index = int(from_stack_number) - 1
    to_stack_index = int(to_stack_number) - 1
    from_stack = stacks[from_stack_index]
    to_stack = stacks[to_stack_index]
    crane_contents = []
    for item_num in range(num_items):
        crane_contents.append(from_stack.pop())
    crane_contents = list(reversed(crane_contents))
    for item in crane_contents:
        to_stack.append(item)


