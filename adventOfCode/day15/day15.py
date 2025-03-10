
with open("data_warehouse.txt", "r") as f:
    list_warehouse = f.read().split("\n")
with open("data_movements.txt", "r") as f:
    str_movements = "".join(f.read().split("\n"))




def get_initial_position(arr_warehouse:list) -> tuple[int]:
    for i,row in enumerate(list_warehouse):
        if row.find("@") != -1:
            return (i, row.find("@"))



def part1():
    # get init pos
    tup_init_pos = get_initial_position(list_warehouse)
    breakpoint()

    # look ahead

    # push box
    pass


def main():
    part1()


if __name__ == "__main__":
    main()