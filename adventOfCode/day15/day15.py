
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




def get_initial_position(list_warehouse:list) -> tuple[int]:
    # returns tuple[int], (irow, icol)
    for i,row in enumerate(list_warehouse):
        if row.find("@") != -1:
            return (i, row.find("@"))



def look_ahead(list_warehouse:list, str_movement:str, 
               curr_pos:tuple[int]) -> str:
    if str_movement == "<":
        return list_warehouse[curr_pos[0]][:curr_pos[1]]
    if str_movement == ">":
        return list_warehouse[curr_pos[0]][curr_pos[1]+1:]
    if str_movement == "^":
        list_warehouse_t = transpose_warehouse(list_warehouse)
        return list_warehouse_t[curr_pos[1]][:curr_pos[0]]
    if str_movement == "v":
        list_warehouse_t = transpose_warehouse(list_warehouse)
        return list_warehouse_t[curr_pos[1]][curr_pos[0]+1:]



def part1():
    # get init pos
    tup_init_pos = get_initial_position(WAREHOUSE_INIT)

    # look ahead
    # test code
    path_ahead = look_ahead(WAREHOUSE_INIT, "^", tup_init_pos)
    breakpoint()

    # check ahead

    # push box
    pass


def main():
    part1()


if __name__ == "__main__":
    main()
    