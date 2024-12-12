"""
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............ (12*12)
^ (0,0)    ^ (0,11)

the coordinate of the topmost "0" is (8, 10)
"""
from itertools import permutations



def get_antennas(data:list[list[str]]) -> set:
    """
    Get all unique antennas on the grid.
    
    Args:
        data (list[list[str]]): the grid.

    Returns:
        set: unique antennas. Each antenna is represented by a string
    """
    set_antennas = {antenna for row in data for antenna in set(row) if antenna!="."}
    return set_antennas



def get_coords(data:list[list[str]], set_antennas:set) -> dict:
    """
    Get the coordinate of all antennas. 
    The bottom left most point of the grid is considered as (0,0).
    
    Args:
        data (list[list[str]]): the grid.
        set_antennas (set): unique antennas.

    Returns:
        dict_coords: key: unique antennas. Value: list of coords (tuple) of
        all locations of the antenna.
        eg: {'0': [(8, 10), (5, 9), (7, 8), (4, 7)], 'A': [(6, 6), (8, 3), (9, 2)]}
    """

    dict_coords = {}
    for antennas in set_antennas:
        dict_coords[antennas] = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] in set_antennas:
                dict_coords[data[i][j]].append( (j, len(data)-1-i) )
    return dict_coords



def jump_over_stationary(coord_jumping:tuple, coord_stationary:tuple) -> tuple:
    """
    The jumping point jumps over the stationary point.
    Calculated by reversing the formula of midpoint. (stationary point is 
    considered as the midpoint.)
    
    Args:
        coord_jumping (tuple(int,int)): the jumping point.
        coord_stationary (tuple(int,int)): the stationary point.

    Returns:
        tuple: the new point after jumping.
    """
    # they are both tuple of two int
    return (2*coord_stationary[0]-coord_jumping[0], 2*coord_stationary[1]-coord_jumping[1] )



def jump_2(coord_jumping:tuple, coord_stationary:tuple, size_width:int, size_height:int):
    """
    The jumping point jumps over the stationary point, and over and over until 
    out of the edge.
    Calculated by accumulating the delta of the two initial points.
    
    Args:
        coord_jumping (tuple(int,int)): the jumping point.
        coord_stationary (tuple(int,int)): the stationary point.
        size_width (int): width of the grid.
        size_height (int): height of the grid.

    Returns:
        tuple: list of new points on edge after jumping.
    """

    delta_x = coord_stationary[0] - coord_jumping[0]
    delta_y = coord_stationary[1] - coord_jumping[1]

    coord_new = coord_jumping
    antinodes = []
    while is_on_edge(coord_new, size_width, size_height):
        coord_new = (coord_new[0]+delta_x, coord_new[1]+delta_y)
        antinodes.append(coord_new)
    # the out of edge antinode is appended at the last iteration
    # so slice it
    return antinodes[:-1]



def is_on_edge(antinode:tuple, size_width:int, size_height:int):
    """
    Check whether the point (antinode) is still on the edge.
    
    Args:
        antinode (tuple(int,int)): the point to be checked.
        size_width (int): width of the grid.
        size_height (int): height of the grid.

    Returns:
        bool: True if the point is still on the edge,
        False if the point falls out of the edge.
    """

    if 0 <= antinode[0] <= size_width and 0 <= antinode[1] <= size_height:
        return True
    else:
        return False



def part_1(path_input:str):
    with open(path_input, "r") as f:
        data =  [list(row) for row in f.read().strip().split("\n")]
    set_antennas = get_antennas(data)
    dict_coords = get_coords(data, set_antennas)
    set_antinodes = set()

    for antenna, coords in dict_coords.items():
        perm = permutations(coords, 2)
        for jump_and_stat in perm:
            antinode = jump_over_stationary(jump_and_stat[0], jump_and_stat[1]) # tuple of two int
            if is_on_edge(antinode, len(data[0])-1, len(data)-1):
                set_antinodes.add(antinode)
    print(len(set_antinodes))
    return set_antinodes



def part_2(path_input:str):
    with open(path_input, "r") as f:
        data =  [list(row) for row in f.read().strip().split("\n")]
    set_antennas = get_antennas(data)
    dict_coords = get_coords(data, set_antennas)
    set_antinodes = set()

    for antenna, coords in dict_coords.items():
        perm = permutations(coords, 2)
        for jump_and_stat in perm:
            set_antinodes.update(set(jump_2(jump_and_stat[0], jump_and_stat[1], len(data[0])-1, len(data)-1)))
    print(len(set_antinodes))
    return set_antinodes



def main():
    path_input = "data.txt"
    part_1(path_input)
    part_2(path_input)



if __name__ == "__main__":
    main()

