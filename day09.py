from typing import Tuple, List, Set, Optional

h_pt: Tuple = (0, 0)
t_pts: Set = set()
knots: List[Tuple] = []


def move_head(instructions: str):
    global h_pt
    direction, distance = instructions.split()
    distance = int(distance)
    match direction:
        case 'R':
            for _ in range(distance):
                h_pt = (h_pt[0] + 1, h_pt[1])
                move_next_knot_if_needed()
        case 'L':
            for _ in range(distance):
                h_pt = (h_pt[0] - 1, h_pt[1])
                move_next_knot_if_needed()
        case 'U':
            for _ in range(distance):
                h_pt = (h_pt[0], h_pt[1] - 1)
                move_next_knot_if_needed()
        case 'D':
            for _ in range(distance):
                h_pt = (h_pt[0], h_pt[1] + 1)
                move_next_knot_if_needed()


def move_next_knot_if_needed():
    global h_pt, knots, t_pts
    leading_knot = h_pt
    for i, trailing_knot in enumerate(knots):
        new_not_position = get_new_knot_position(leading_knot, trailing_knot)
        if new_not_position:
            knots[i] = new_not_position
            leading_knot = new_not_position
        else:
            break
    t_pts.add(knots[-1])


def get_new_knot_position(leading_knot, trailing_knot) -> Optional[Tuple]:
    """ Returns the new position of the trailing knot, or None if it does not need to move"""
    move_x = 0
    move_y = 0
    dist_y = leading_knot[0] - trailing_knot[0]
    dist_x = leading_knot[1] - trailing_knot[1]
    if abs(dist_x) <= 1 and abs(dist_y) <= 1:
        return None
    if dist_y:
        move_y = -1 if dist_y < 0 else 1
    if dist_x:
        move_x = -1 if dist_x < 0 else 1
    return trailing_knot[0] + move_y, trailing_knot[1] + move_x


def move_all_the_things(instructions, knot_count=1):
    global knots, h_pt, t_pts
    h_pt = (0, 0)
    t_pts = set()
    knots = []
    for knot in range(knot_count):
        knots.append((0, 0))
    t_pts.add(knots[-1])
    for instruction in instructions:
        move_head(instruction)
    return len(t_pts)