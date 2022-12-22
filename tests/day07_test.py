from typing import List
import pytest

import day07
day = "07"

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


def test_day07_sample(sample_list):
    assert day07.get_sum_of_small_dirs(sample_list) == 95437


def test_day07_real(real_list):
    assert day07.get_sum_of_small_dirs(real_list) == 1517599


def test_day07_delete_dir_sample(sample_list):
    assert day07.delete_directory(sample_list) == 24933642


def test_day07_delete_dir_real(real_list):
    assert day07.delete_directory(real_list) == 2481982
