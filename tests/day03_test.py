from typing import List
import pytest

import day03


@pytest.fixture
def sample_list() -> List:
    return [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]


@pytest.fixture
def real_list() -> List:
    filename = "data/day03.txt"
    real_list = []
    with open(filename, 'r') as file_handle:
        for line in file_handle:
            real_list.append(line.strip('\n'))
    return real_list


def test_get_priority(sample_list):
    line_1 = sample_list[0]
    assert day03.get_priority(line_1) == 16


def test_get_sum_sample(sample_list):
    assert day03.sum_of_priorities(sample_list) == 157


def test_get_sum_real(real_list):
    assert day03.sum_of_priorities(real_list) == 7568


def test_get_elf_group_sum_sample(sample_list):
    assert day03.sum_of_group_priorities(sample_list) == 70


def test_get_elf_group_sum(real_list):
    assert day03.sum_of_group_priorities(real_list) == 2780
