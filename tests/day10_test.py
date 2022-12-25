from typing import List
import pytest

import day10
day = "10"

sample_file = f"data/day{day}_sample.txt"
real_file = f"data/day{day}.txt"


def get_list(filename):
    real_list = []
    with open(filename, 'r') as file_handle:
        for line in file_handle:
            real_list.append(line.strip('\n'))
    return real_list


@pytest.fixture
def sample_list() -> List:
    return get_list(sample_file)


@pytest.fixture
def real_list() -> List:
    return get_list(real_file)


def test_signal_strength_sample(sample_list):
    assert day10.get_signal_strength(sample_list) == 13140


def test_signal_strength(real_list):
    assert day10.get_signal_strength(real_list) == 14560
