def get_priority(line) -> int:
    half_len = int(len(line) / 2)
    left_half = line[:half_len]
    right_half = line[half_len:]
    found_char = ''
    for char in left_half:
        if char in right_half:
            found_char = char
            break
    return get_char_value(found_char)


def get_char_value(found_char) -> int:
    if found_char.isupper():
        letter_val = ord(found_char) - ord('A') + 27
    else:
        letter_val = ord(found_char) - ord('a') + 1

    return letter_val


def sum_of_priorities(rucksack_contents) -> int:
    pri_sum = 0
    for line in rucksack_contents:
        pri_sum += get_priority(line)
    return pri_sum


def get_badge_group_priority(group):
    assert len(group) == 3
    found_char = ''
    for char in group[0]:
        if char in group[1] and char in group[2]:
            found_char = char
    return get_char_value(found_char)


def sum_of_group_priorities(rucksack_contents):
    line_no = 1
    sum_of_group_pri = 0
    group_of_lines = []
    for line in rucksack_contents:
        if line_no < 3:
            group_of_lines.append(line)
            line_no += 1
        elif line_no == 3:
            group_of_lines.append(line)
            sum_of_group_pri += get_badge_group_priority(group_of_lines)
            line_no = 1
            group_of_lines = []
    return sum_of_group_pri
