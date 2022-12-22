from typing import List
import numpy as np

def get_column(grid: List, column_number):
    column = []
    for i, row in enumerate(grid):
        column.append(grid[i][column_number])
    return column


def get_trees_in_direction(direction, grid, column, row) -> List:
    trees: List = []
    if direction == 'up':
        for tree_row, tree_height in enumerate(get_column(grid, column)):
            if tree_row < row:
                trees.append(tree_height)
        return trees
    if direction == 'down':
        for tree_row, tree_height in enumerate(get_column(grid, column)):
            if tree_row > row:
                trees.append(tree_height)
        return trees
    if direction == 'left':
        for tree_column, tree_height in enumerate(grid[row]):
            if tree_column < column:
                trees.append(tree_height)
        return trees
    if direction == 'right':
        for tree_column, tree_height in enumerate(grid[row]):
            if tree_column > column:
                trees.append(tree_height)
        return trees


def visible_up_or_down(grid, column, row, current_height) -> bool:
    visible_up: bool = True
    for tree_height in get_trees_in_direction('up', grid, column, row):
        if tree_height >= current_height:
            visible_up = False
    visible_down: bool = True
    for tree_height in get_trees_in_direction('down', grid, column, row):
        if tree_height >= current_height:
            visible_down = False
    return visible_down or visible_up


def visible_left_or_right(grid, row, column, current_height) -> bool:
    visible_left: bool = True
    for tree_height in get_trees_in_direction('left', grid, column, row):
        if tree_height >= current_height:
            visible_left = False
    visible_right: bool = True
    for tree_height in get_trees_in_direction('right', grid, column, row):
        if tree_height >= current_height:
            visible_right = False
    return visible_left or visible_right


def score_in_direction(direction, grid, row, column, current_height) -> int:
    score: int = 0
    trees_to_search = get_trees_in_direction(direction, grid, column, row)
    if direction == 'up' or direction == 'left':
        trees_to_search = reversed(trees_to_search)
    for tree_height in trees_to_search:
        score += 1
        if tree_height >= current_height:
            break
    return score


def score_in_all_directions(grid, row, column, current_height) -> int:
    score: List[int] = []
    for direction in ['up', 'left', 'right', 'down']:
        score.append(score_in_direction(direction, grid, row, column, current_height))
    return np.product(score)


def visible_tree_count(tree_grid, get_visibility_score=False):
    num_columns = len(tree_grid[0])
    num_rows = len(tree_grid)
    grid: List[List] = []
    for row in tree_grid:
        grid.append(list(row))
    visible_trees: int = 0
    best_visibility_score: int = 0
    for row in range(1, num_rows-1):
        for column in range(1, num_columns - 1):
            current_tree_height: int = grid[row][column]
            is_visible = visible_up_or_down(grid, column, row, current_tree_height)
            if not is_visible:
                is_visible = visible_left_or_right(grid, row, column, current_tree_height)
            if is_visible:
                visible_trees += 1
            if get_visibility_score:
                best_visibility_score = max(
                    best_visibility_score,
                    score_in_all_directions(grid, row, column, current_tree_height)
                )
    visible_trees += 2*(num_columns + num_rows) - 4
    if get_visibility_score:
        return best_visibility_score
    return visible_trees


