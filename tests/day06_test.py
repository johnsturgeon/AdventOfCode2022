from typing import List
import pytest

import day06
day = "06"

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


def test_packet_position_sample(sample_list):
    assert day06.get_packet_position(sample_list) == 7


def test_packet_position_real(real_list):
    assert day06.get_packet_position(real_list) == 1848


def test_packet_position_real_p2(real_list):
    assert day06.get_packet_position(real_list, key_len=14) == 2308

