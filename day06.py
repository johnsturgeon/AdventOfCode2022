def get_packet_position(position_list, key_len=4):
    assert len(position_list) == 1
    sequence = position_list[0]
    buffer_to_check: str = ""
    for index, char in enumerate(sequence):
        buffer_to_check += char
        if len(buffer_to_check) < key_len:
            continue
        if len(set(buffer_to_check)) == len(buffer_to_check):
            return index + 1
        if len(buffer_to_check) == key_len:
            buffer_to_check = buffer_to_check[1:]
