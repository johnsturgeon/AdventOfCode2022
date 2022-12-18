from typing import List


def most_calories(elvin_calorie_list: List) -> int:
    max_cals = 0
    current_elf_cals = 0
    for cals in elvin_calorie_list:
        if not cals or cals == '\n':
            current_elf_cals = 0
            continue
        current_elf_cals += int(cals)
        max_cals = max(current_elf_cals, max_cals)
    return max_cals


def top_three_calories(elvin_calorie_list: List) -> int:
    current_elf_cals = 0
    elf_cal_list: List[int] = []
    sum_of_top_three = 0
    for cals in elvin_calorie_list:
        if not cals or cals == '\n':
            elf_cal_list.append(current_elf_cals)
            current_elf_cals = 0
        else:
            current_elf_cals += int(cals)
    elf_cal_list.sort(reverse=True)
    for cal_total in elf_cal_list[:3]:
        sum_of_top_three += cal_total
    return sum_of_top_three



