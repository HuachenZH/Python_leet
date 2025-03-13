
with open("data_warehouse_small.txt", "r") as f:
    WAREHOUSE_INIT = f.read().strip().split("\n") # list[str]
with open("data_movements_small.txt", "r") as f:
    MOVEMENTS = "".join(f.read().strip().split("\n")) # str


def transpose_warehouse(list_warehouse:list) -> list[str]:
    # if you run the list comprehension in pdb, it will say
    # NameError: name 'list_warehouse' is not defined
    # However if you run it in interactive session, it will be fine.
    return [ "".join([row[icol] for row in list_warehouse]) 
            for icol in range(len(list_warehouse))]




def get_robot_position(list_warehouse:list) -> tuple[int]:
    # returns tuple[int], (irow, icol)
    for i,row in enumerate(list_warehouse):
        if row.find("@") != -1:
            return (i, row.find("@"))



def look_ahead_including_self(list_warehouse:list, str_movement:str, 
               curr_pos:tuple[int]) -> str:
    # the returned string should be what the robot see, from left to
    # right. 
    # If look left and warehouse is like
    # #..O.@
    # then it should return .O..#
    # so while looking left or up, reverse the returned string
    if str_movement == "<":
        return list_warehouse[curr_pos[0]][:curr_pos[1]+1][::-1]
    if str_movement == ">":
        return list_warehouse[curr_pos[0]][curr_pos[1]:]
    if str_movement == "^":
        list_warehouse_t = transpose_warehouse(list_warehouse)
        return list_warehouse_t[curr_pos[1]][:curr_pos[0]+1][::-1]
    if str_movement == "v":
        list_warehouse_t = transpose_warehouse(list_warehouse)
        return list_warehouse_t[curr_pos[1]][curr_pos[0]:]




def calculate_new_path_ahead(warehouse:list[str], movement:str, 
                       tup_robot_pos:tuple[int], path_ahead:str) -> str:
    # returns the new path ahead

    # move one
    if path_ahead[1:][0] == ".":
        # permute first and second character
        # @.. becomes 
        # .@.
        return path_ahead[1] + path_ahead[0] + path_ahead[2:]
    # push one
    elif path_ahead[1:][:2] == "O.":
        # @O..OO# becomes
        # .@O.OO#
        return  path_ahead[2] + path_ahead[:2] + path_ahead[3:]
    # cannot move, wall ahead
    elif path_ahead[1:][0] == "#":
        return path_ahead
    # push several, or cannot push
    elif path_ahead[1:][:2] == "OO" and path_ahead.count("O") > 1:
        # @OOOO..O#
        # @OOOO#..O#
        # @OO...#..#
        if path_ahead.find(".") < path_ahead.find("#"):
            # There is at least a space appears before wall. Can push.
            return "." + path_ahead[:path_ahead.find(".")] + path_ahead[path_ahead.find(".")+1:]
        else:
            # cannot push
            return path_ahead
    # other cases
    else:
        breakpoint()
        raise RuntimeError(f"Unexpected case, path ahead: {path_ahead}")
    


def replace_new_path(warehouse:list[str], movement:str,
                     tup_robot_pos:tuple[int], new_path_ahead:str) -> list[str]:
    # returns new warehouse
    # if move is ">", horizontal, keep order
    if movement == ">":
        line = warehouse[tup_robot_pos[0]]
        warehouse[tup_robot_pos[0]] = line[:tup_robot_pos[1]] + new_path_ahead
    # if move is "<", horizontal, reverse order
    if movement == "<":
        line = warehouse[tup_robot_pos[0]]
        breakpoint()
        warehouse[tup_robot_pos[0]] = new_path_ahead[::-1] + line[tup_robot_pos[1]+1:]
        breakpoint()
        print("-"*79)
    # if move is "v", vertical, transpose and keep order
    # if move is "^", vertical, transpose then reverse order
    return warehouse




def part1():
    print("\n".join(WAREHOUSE_INIT))
    warehouse = WAREHOUSE_INIT

    # look ahead
    # initial pos
    tup_robot_pos = get_robot_position(WAREHOUSE_INIT)
    for movement in MOVEMENTS:
        path_ahead = look_ahead_including_self(warehouse, movement, tup_robot_pos)
        new_path_ahead = calculate_new_path_ahead(warehouse, movement, tup_robot_pos, path_ahead)
        if new_path_ahead != path_ahead:
            warehouse = replace_new_path(warehouse, movement, tup_robot_pos, new_path_ahead)
        tup_robot_pos = get_robot_position(warehouse)


    # push box
    pass


def main():
    part1()


if __name__ == "__main__":
    main()
    


# to_resume:
# breakpoint at line 79, unexpected case: @O#
# need to rewrite the logic in calculate_new_path_ahead(), combine some conditions
# if "O" in path_ahead, if "." is found before "#", then can move
# notice that if "." does not existe it returns -1 which is always < find("#")

# print("\n".join(warehouse))