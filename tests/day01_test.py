from typing import List
import pytest

import day01


@pytest.fixture
def sample_list() -> List:
    return ["1000",
            "2000",
            "3000",
            "",
            "4000"
            "",
            "5000",
            "6000",
            "",
            "7000",
            "8000",
            "9000",
            "",
            "10000"]


@pytest.fixture
def real_list() -> List:
    filename = "data/day01.txt"
    real_list = []
    with open(filename, 'r') as file_handle:
        for line in file_handle:
            real_list.append(line)
    return real_list


def test_day_01_sample(sample_list):
    assert day01.most_calories(sample_list) == 24000


def test_day_01_real(real_list):
    assert day01.most_calories(real_list) == 71934


def test_day_01_part_2_sample(sample_list):
    assert day01.top_three_calories(sample_list) == 45000


def test_day_01_part_2_real(real_list):
    assert day01.top_three_calories(real_list) == 26366

