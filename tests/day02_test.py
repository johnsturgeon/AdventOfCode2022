from typing import List
import pytest

import day02


@pytest.fixture
def sample_list() -> List:
    return [
        "A Y",
        "B X",
        "C Z"
    ]


@pytest.fixture
def real_list() -> List:
    filename = "data/day02.txt"
    real_list = []
    with open(filename, 'r') as file_handle:
        for line in file_handle:
            real_list.append(line.strip('\n'))
    return real_list


def test_day_02_sample(sample_list):
    assert day02.get_score(sample_list) == 15


def test_day_02_real(real_list):
    assert day02.get_score(real_list) == 12458


def test_day_02_part_2_sample(sample_list):
    assert day02.get_scores_harder(sample_list) == 12


def test_day_02_part_2_real(real_list):
    assert day02.get_scores_harder(real_list) == 12683

