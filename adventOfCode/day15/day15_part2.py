from day15_part1 import get_robot_position
from day15_part1 import look_ahead_including_self
from day15_part1 import calculate_new_path_ahead
from day15_part1 import replace_new_path




with open("data/data_warehouse_large.txt", "r") as f:
    # list[list[str]]
    # WAREHOUSE_INIT = [ list(row) for row in f.read().strip().split("\n") ]

    # twice as wide, list[str]
    WAREHOUSE_INIT = [ row.replace("#","##").replace("O","[]").replace(".","..").replace("@","@.") for row in f.read().strip().split("\n") ]

with open("data/data_movements_part1.txt", "r") as f:
    MOVEMENTS = "".join(f.read().strip().split("\n")) # str



def calculate_lanternfish_coordinates_part2(warehouse:list[str]) -> str:
    return sum([i*100+j  for i,line in enumerate(warehouse) for j,char in enumerate(line) if char=="[" or char=="]"])



def find_pairing_horizontally(box:str, tup_robot_pos:tuple[int]):
    if box == "[":
        return (tup_robot_pos[0], tup_robot_pos[1]+1)
    if box == "]":
        return (tup_robot_pos[0], tup_robot_pos[1]-1)



def _up(tup_pos:tuple[int]):
    breakpoint()
    return (tup_pos[0]-1, tup_pos[1])


def _down(tup_pos:tuple[int]):
    return (tup_pos[0]+1, tup_pos[1])


def _left(tup_pos:tuple[int]):
    return (tup_pos[0], tup_pos[1]-1)


def _right(tup_pos:tuple[int]):
    return (tup_pos[0], tup_pos[1]+1)


def _get_shape(warehouse:list[str], pos:tuple[int]):
    return warehouse[pos[0]][pos[1]]



def find_next_line_boxes(warehouse:list[str], curr_box_positions:list[tuple[int]]):
    # currently "next" means up
    nextline_box_positions = []
    for pos in curr_box_positions:
        nextline_box_positions.append(_up(pos))
        adj_shape = _get_shape(warehouse, _up(pos))
        if adj_shape in "[]":
            nextline_box_positions.append(_up(pos))
            if adj_shape != _get_shape(warehouse, pos):
                nextline_box_positions.append(find_pairing_horizontally(_up(pos)))
    return nextline_box_positions




def can_push_vertically(warehouse:list[str], tup_robot_pos:tuple[int]):
    flag = True
    while flag:
        # to_resume: argument error, tup_robot_pos is tuple not list.
        # at first iteration, it should be a list
        nextline_box_positions = find_next_line_boxes(warehouse, tup_robot_pos)
        if not nextline_box_positions and len(nextline_box_positions) == 0:
            flag = False
            breakpoint()




def main():
    warehouse = WAREHOUSE_INIT

    tup_robot_pos = get_robot_position(WAREHOUSE_INIT)
    for movement in MOVEMENTS:
        if movement == "<" or movement == ">":
            # part 1
            path_ahead = look_ahead_including_self(warehouse, movement, tup_robot_pos)
            new_path_ahead = calculate_new_path_ahead(warehouse, movement, tup_robot_pos, path_ahead)
            if new_path_ahead != path_ahead:
                warehouse = replace_new_path(warehouse, movement, tup_robot_pos, new_path_ahead)
            tup_robot_pos = get_robot_position(warehouse)

        if movement == "^" or movement == "v":
            can_push_vertically(warehouse, tup_robot_pos)
            # update warehouse
            warehouse = warehouse

    sumcoord = calculate_lanternfish_coordinates_part2(warehouse)
    print(sumcoord)




if __name__ == "__main__":
    main()

