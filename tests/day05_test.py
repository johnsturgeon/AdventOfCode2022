from typing import List
import pytest

import day05


@pytest.fixture
def sample_list() -> List:
    filename = "data/day05_sample.txt"
    real_list = []
    with open(filename, 'r') as file_handle:
        for line in file_handle:
            real_list.append(line.strip('\n'))
    return real_list


@pytest.fixture
def real_list() -> List:
    filename = "data/day05.txt"
    real_list = []
    with open(filename, 'r') as file_handle:
        for line in file_handle:
            real_list.append(line.strip('\n'))
    return real_list


def test_get_stack_data(sample_list):
    stack_list = day05.get_stack_list(sample_list)
    instruction_list = day05.get_instruction_list(sample_list, len(stack_list))
    starting_stacks = day05.get_starting_stacks(stack_list)
    for instruction in instruction_list:
        day05.update_stack(starting_stacks, instruction)
    message: str = ""
    for stack in starting_stacks:
        message += str(stack[-1])
    print(message)


def test_get_stack_data_real(real_list):
    stack_list = day05.get_stack_list(real_list)
    instruction_list = day05.get_instruction_list(real_list, len(stack_list))
    starting_stacks = day05.get_starting_stacks(stack_list)
    for instruction in instruction_list:
        day05.update_stack(starting_stacks, instruction)
    message: str = ""
    for stack in starting_stacks:
        message += str(stack[-1])
    print(message)


def test_get_queue_data_sample(sample_list):
    stack_list = day05.get_stack_list(sample_list)
    instruction_list = day05.get_instruction_list(sample_list, len(stack_list))
    starting_stacks = day05.get_starting_stacks(stack_list)
    for instruction in instruction_list:
        day05.update_queue(starting_stacks, instruction)
    message: str = ""
    for stack in starting_stacks:
        message += str(stack[-1])
    print(message)


def test_get_queue_data_real(real_list):
    stack_list = day05.get_stack_list(real_list)
    instruction_list = day05.get_instruction_list(real_list, len(stack_list))
    starting_stacks = day05.get_starting_stacks(stack_list)
    for instruction in instruction_list:
        day05.update_queue(starting_stacks, instruction)
    message: str = ""
    for stack in starting_stacks:
        message += str(stack[-1])
    print(message)

