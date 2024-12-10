

def check_obstacle_ahead(head:str, pos:tuple, data:list[str]) -> bool:
    """
    Check if there is an obstacle in the direction the head is facing.
    - ^: north face (same column, previous row)
    - >: east face (same row, next column)
    - v: south face (same column, next row)
    - <: west face (same row, previous column)

    Args:
        head (str): Direction character (^, >, v, or <)
        pos (tuple): Current (row, col) position
        data (list[str]): Grid data containing obstacles marked with #

    Returns:
        bool: True if obstacle ahead, False if path is clear

    Raises:
        ValueError: If head is not one of ^, >, v, <
    """

    if head == "^":
        return data[pos[0]-1][pos[1]] == "#"
    elif head == ">":
        return data[pos[0]][pos[1]+1] == "#"
    elif head == "v":
        return data[pos[0]+1][pos[1]] == "#"
    elif head == "<":
        return data[pos[0]][pos[1]-1] == "#"
    else:
        raise ValueError("Head must be one of ^ > v <")



def go_ahead(head:str, pos:tuple) -> tuple:
    """
    Calculate the next position based on the current heading direction.
    
    Args:
        head (str): Direction character (^, >, v, or <)
        pos (tuple): Current (row, col) position

    Returns:
        tuple: Next (row, col) position after moving one step in heading direction

    Raises:
        ValueError: If head is not one of ^, >, v, <
    """

    # return the next position
    if head == "^":
        return (pos[0]-1, pos[1])
    elif head == ">":
        return (pos[0], pos[1]+1)
    elif head == "v":
        return (pos[0]+1, pos[1])
    elif head == "<":
        return (pos[0], pos[1]-1)
    else:
        raise ValueError("Head must be one of ^ > v <")



def turn_right(head:str) -> str:
    """
    Return the next direction after turning right from current heading.
    
    Args:
        head (str): Current direction character (^, >, v, or <)

    Returns:
        str: Next direction character after turning right (^ -> >, > -> v, v -> <, < -> ^)

    Raises:
        ValueError: If head is not one of ^, >, v, <
    """
    chainsmoker = "^>v<"
    return chainsmoker[(chainsmoker.find(head)+1) % len(chainsmoker)]



def check_edge_ahead(head:str, pos:tuple, height:int, width:int) -> bool:
    """
    Check if moving one step in current heading direction would go off the edge.
    
    Args:
        head (str): Direction character (^, >, v, or <)
        pos (tuple): Current (row, col) position
        height (int): Number of rows in the grid (1-indexed)
        width (int): Number of columns in the grid (1-indexed)

    Returns:
        bool: True if next step would go off edge, False if next step is still on grid

    Raises:
        ValueError: If head is not one of ^, >, v, <
    """
    if head == "^":
        return pos[0]-1 < 0
    elif head == ">":
        return pos[1]+1 >= width
    elif head == "v":
        return pos[0]+1 >= height
    elif head == "<":
        return pos[1]-1 < 0
    else:
        raise ValueError("Head must be one of ^ > v <")



def part_1(data:list[list[str]]):
    # initial position 
    pos = next((i, "".join(row).find("^")) for i, row in enumerate(data) if "^" in row)
    
    head = "^"
    while not check_edge_ahead(head, pos, len(data), len(data[0])):
        # If obstacle ahead, turn right
        if check_obstacle_ahead(head, pos, data):
            head = turn_right(head)
        # If nothing ahead, go
        else:
            data[pos[0]][pos[1]] = "X"
            pos = go_ahead(head, pos)
            # Guard quits
     
    # Count number of X
    res = "\n".join(["".join(row) for row in data]).count("X")
    res += 1 # the last position hasn't been updated to "X" before leaving the while loop
    print(res)



def part_2(path_input:str):
    with open(path_input, "r", encoding="utf-8") as f:
        data = [list(row) for row in f.read().strip().split("\n")]

    res = 0
    pos = next((i, "".join(row).find("^")) for i, row in enumerate(data) if "^" in row)
    head = "^"
    breakpoint()

    for row in data:
        for icol, column in enumerate(row):
            if column == ".":
                # Set obstacle
                row[icol] = "O"
                is_stuck = False
                
                
                while not check_edge_ahead(head, pos, len(data), len(data[0])) and not is_stuck:
                    if head == "^":
                        taxi = { "^": 0,
                         ">": 0,
                         "v": 0,
                         "<": 0
                        }
                    # if obstable ahead, turn righ
                    if check_obstacle_ahead(head, pos, data):
                        head = turn_right(head)
                        if taxi["^"] == taxi[">"] == taxi["v"] == taxi["<"]:
                            is_stuck = True
                            res += 1
                    # if nothing ahead, go
                    else:
                        data[pos[0]][pos[1]] = "X"
                        pos = go_ahead(head, pos)
                        taxi[head] = taxi[head] + 1

                # Remove obstacle
                row[icol] = "."

    print(res)



def main():
    path_input = "sample.txt"

    with open(path_input, "r", encoding="utf-8") as f:
        data = [list(row) for row in f.read().strip().split("\n")]

    part_1(data)

    part_2(path_input)
    

if __name__ == "__main__":
    main()




