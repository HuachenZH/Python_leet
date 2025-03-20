from day15_part1 import get_robot_position
from day15_part1 import look_ahead_including_self as look_ahead_horizontal_including_self
from day15_part1 import calculate_lanternfish_coordinates
from day15_part1 import replace_new_path as replace_new_path_horizontal


with open("data/data_warehouse_large.txt", "r") as f:
    # list[list[str]]
    WAREHOUSE_INIT = [ list(row) for row in f.read().strip().split("\n") ]
with open("data/data_movements_large.txt", "r") as f:
    MOVEMENTS = "".join(f.read().strip().split("\n")) # str

for row in WAREHOUSE_INIT:
    for j in range(len(row)):
        if row[j] == "#": row[j] = "##"
        if row[j] == "O": row[j] = "[]"
        if row[j] == ".": row[j] = ".."
        if row[j] == "@": row[j] = "@."
WAREHOUSE_INIT = ["".join(row) for row in WAREHOUSE_INIT ]



def calculate_new_path_ahead_horizontal(path_ahead:str) -> str:
    # returns the new path ahead
    # path_ahead includes robot itself "@", 
    # path_ahead[0] is always "@".

    # Nothing ahead, move one
    if path_ahead[1] == ".":
        return ".@" + path_ahead[2:]
    
    # Wall ahead, cannot move
    elif path_ahead[1] == "#":
        return path_ahead
    
    # Box ahead, can push, e.g.:
    # @[]....# (movemnt is ">")
    # @][....# (movemnt is "<")
    elif ((path_ahead[1]=="[" or path_ahead[1]=="]")
          and "." in path_ahead
          and path_ahead.find(".") < path_ahead.find("#")):
        return "." + path_ahead[:path_ahead.find(".")] + path_ahead[path_ahead.find(".")+1:] 

    # Box ahead, cannot push, no space, e.g.:
    # @[][][]# (movement is ">")
    # @][][][# (movement is "<")
    elif ( (path_ahead[1]=="[" or path_ahead[1]=="]")
          and path_ahead.find(".")==-1):
        return path_ahead

    # Box ahead, cannot push, wall before space, e.g.:
    # @[]#......# (movment is ">")
    # @][#......# (movment is "<")
    elif ( (path_ahead[1]=="[" or path_ahead[1]=="]")
          and path_ahead.find(".") > path_ahead.find("#")):
        return path_ahead
    
    # other cases
    else:
        raise RuntimeError(f"Unexpected case, path ahead: {path_ahead}")



def main():
    print("start:")
    print("\n".join(WAREHOUSE_INIT) + "\n")
    warehouse = WAREHOUSE_INIT

    tup_robot_pos = get_robot_position(warehouse)
    for movement in MOVEMENTS:
        # if horizontal
        if movement == "<" or movement == ">":
            # horizontal lookup
            path_ahead = look_ahead_horizontal_including_self(warehouse, movement, tup_robot_pos)
            # horizontal check
            new_path_ahead = calculate_new_path_ahead_horizontal(path_ahead)
            # horizontal replace
            if new_path_ahead != path_ahead:
                warehouse = replace_new_path_horizontal(warehouse, movement, tup_robot_pos, new_path_ahead)

        # if vertical
            # vertical lookup
            # vertical check
            # vertical replace
        tup_robot_pos = get_robot_position(warehouse)
    print("end:")
    print("\n".join(warehouse) + "\n")



if __name__ == "__main__":
    main()


# print("\n".join(warehouse))