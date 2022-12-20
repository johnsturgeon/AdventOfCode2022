from typing import List
import pytest

import day04


@pytest.fixture
def sample_list() -> List:
    filename = "data/day04_sample.txt"
    real_list = []
    with open(filename, 'r') as file_handle:
        for line in file_handle:
            real_list.append(line.strip('\n'))
    return real_list


@pytest.fixture
def real_list() -> List:
    filename = "data/day04.txt"
    real_list = []
    with open(filename, 'r') as file_handle:
        for line in file_handle:
            real_list.append(line.strip('\n'))
    return real_list


def test_num_intersections_sample(sample_list):
    assert day04.get_num_intersections(sample_list) == 2


def test_num_intersections_real(real_list):
    assert day04.get_num_intersections(real_list) == 503


def test_num_intersections_real_at_all(real_list):
    assert day04.get_num_intersections_at_all(real_list) == 827
