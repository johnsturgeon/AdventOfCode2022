from typing import List
import pytest

import day08
day = "08"

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


def test_visible_tree_count_sample(sample_list):
    assert day08.visible_tree_count(sample_list) == 21


def test_visible_tree_count_real(real_list):
    assert day08.visible_tree_count(real_list) == 1538


def test_visibility_score_sample(sample_list):
    assert day08.visible_tree_count(sample_list, get_visibility_score=True) == 8


def test_visibility_score_real(real_list):
    assert day08.visible_tree_count(real_list, get_visibility_score=True) == 496125
