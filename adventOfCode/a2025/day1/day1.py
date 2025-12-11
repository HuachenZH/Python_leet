# convention :
# left rotation  = substraction
# right rotation = addition


import re


def retrieve_rotation_magnitude(rotation:str) -> int:
    return int(re.search(r"\d+", rotation).group())



def rotate(curr_pos:int, rotation:str) -> int:
    if rotation == "":
        raise ValueError("Rotation string cannot be emtpy")

    # in input, there are entries like L970, R687
    rotation_magnitude = retrieve_rotation_magnitude(rotation) % 100
    if rotation.upper().startswith("L"):
        return left_rotate(curr_pos, rotation_magnitude)
    if rotation.upper().startswith("R"):
        return right_rotate(curr_pos, rotation_magnitude)



def left_rotate(curr_pos:int, rotation_magnitude:int):
    new_pos = curr_pos - rotation_magnitude
    if new_pos >= 0:
        return new_pos
    else:
        return 100 - (-1 * new_pos)



def right_rotate(curr_pos:int, rotation_magnitude:int):
    new_pos = curr_pos + rotation_magnitude
    if new_pos < 100:
        return new_pos
    else:
        return new_pos % 100



def main():
    with open("input.txt", "r") as f:
        input_ = f.read().strip()

    rotations = input_.strip().split("\n")

    res = 0
    curr_pos = 50
    for rotation in rotations:
        curr_pos = rotate(curr_pos, rotation)
        if curr_pos == 0:
            res += 1

    print(res)

    


if __name__ == "__main__":
    main()
