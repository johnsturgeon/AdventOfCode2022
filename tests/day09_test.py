from typing import List
import pytest

import day09
day = "09"

sample_file = f"data/day{day}_sample.txt"
sample_2_file = f"data/day{day}_sample_2.txt"
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
def sample_2_list() -> List:
    return get_list(sample_2_file)


@pytest.fixture
def real_list() -> List:
    return get_list(real_file)


def test_move_all_the_things_sample(sample_list):
    assert day09.move_all_the_things(sample_list) == 13


def test_move_all_the_things(real_list):
    assert day09.move_all_the_things(real_list) == 6391


def test_move_all_the_things_with_knots_sample(sample_2_list):
    assert day09.move_all_the_things(sample_2_list, knot_count=9) == 36


def test_move_all_the_things_with_knots(real_list):
    assert day09.move_all_the_things(real_list, knot_count=9) == 2593

