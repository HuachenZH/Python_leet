from day15_part1 import get_robot_position
from day15_part1 import look_ahead_including_self
from day15_part1 import calculate_new_path_ahead
from day15_part1 import replace_new_path




with open("data/data_warehouse_large.txt", "r") as f:
    # list[list[str]]
    # WAREHOUSE_INIT = [ list(row) for row in f.read().strip().split("\n") ]

    # twice as wide, list[str]
    WAREHOUSE_INIT = [ row.replace("#","##").replace("O","[]").replace(".","..").replace("@","@.") for row in f.read().strip().split("\n") ]
    breakpoint()

with open("data/data_movements_part1.txt", "r") as f:
    MOVEMENTS = "".join(f.read().strip().split("\n")) # str

for row in WAREHOUSE_INIT:
    for j in range(len(row)):
        if row[j] == "#": row[j] = "##"
        if row[j] == "O": row[j] = "[]"
        if row[j] == ".": row[j] = ".."
        if row[j] == "@": row[j] = "@."
WAREHOUSE_INIT = ["".join(row) for row in WAREHOUSE_INIT ]




def calculate_lanternfish_coordinates_part2(warehouse:list[str]) -> str:
    return sum([i*100+j  for i,line in enumerate(warehouse) for j,char in enumerate(line) if char=="[" or char=="]"])




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
            pass

    sumcoord = calculate_lanternfish_coordinates_part2(warehouse)
    print(sumcoord)




if __name__ == "__main__":
    main()

