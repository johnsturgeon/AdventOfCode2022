from typing import List


def range_in_range(r1, r2, at_all=False) -> int:
    r1_s, r1_e = r1.split('-')
    r2_s, r2_e = r2.split('-')
    list_1 = list(range(int(r1_s), int(r1_e) + 1))
    list_2 = list(range(int(r2_s), int(r2_e) + 1))
    intersected_list = intersection(list_1, list_2)
    intersected_list.sort()
    if at_all and intersected_list:
        return 1
    if intersected_list == list_1 or intersected_list == list_2:
        return 1
    return 0


def intersection(lst1, lst2) -> List:
    return list(set(lst1) & set(lst2))


def get_num_intersections(assignment_list) -> int:
    num_intersections: int = 0
    for assignment in assignment_list:
        elf_1, elf_2 = assignment.split(',')
        num_intersections += range_in_range(elf_1, elf_2)
    return num_intersections

def get_num_intersections_at_all(assignment_list) -> int:
    num_intersections: int = 0
    for assignment in assignment_list:
        elf_1, elf_2 = assignment.split(',')
        num_intersections += range_in_range(elf_1, elf_2, at_all=True)
    return num_intersections
