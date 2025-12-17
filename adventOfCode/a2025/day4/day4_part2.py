def preprocess_grid(grid:list[str]) -> list[str]:
    # Preprocess grid, add four edges of "...."
    grid = ["."+row+"." for row in grid]
    grid = [len(grid[0]) * "."] + grid + [len(grid[0]) * "."]
    return grid



def transform_grid_to_zero_and_one(grid:list[str]) -> list[list[int]]:
    # replace string in grid
    # @ --> 1
    # . --> 0
    grid = "\n".join(grid).strip().replace("@","1").replace(".","0").split("\n")
    grid = [[int(col) for col in row] for row in grid]
    return grid



def count_adj_sweetrolls(grid:list[str], irow:int, icol:int) -> int:
    count_adj_sweetroll = (grid[irow-1][icol-1] + grid[irow-1][icol] + grid[irow-1][icol+1]
                         +grid[irow][icol-1] +          0           + grid[irow][icol+1]
                         +grid[irow+1][icol-1] + grid[irow+1][icol] + grid[irow+1][icol+1])
    return count_adj_sweetroll

        

def remove_sweetrolls(grid:list[list[int]], sweetrolls_to_remove:list[tuple[int]]) -> list[list[int]]:
    for coord in sweetrolls_to_remove:
        grid[coord[0]][coord[1]] = 0
    return grid


def main():
    with open("input_day4.txt", "r") as f:
        grid = f.read().strip().split("\n")
    
    #print("[*] before preprocessing, grid is:")
    #print("\n".join(grid))
    grid = preprocess_grid(grid)
    #print("[*] after preprocessing, grid is:")
    #print("\n".join(grid))

    grid = transform_grid_to_zero_and_one(grid)

    res = 0
    sweetrolls_to_remove = [1] # to start the first iteration
    while len(sweetrolls_to_remove) > 0:
        sweetrolls_to_remove = [] # list of index. list[tuple[int]]
        # Do not iterate over newly added "...." edge
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[i])-1):
                if grid[i][j] == 1:
                    if count_adj_sweetrolls(grid, i, j) < 4:
                        sweetrolls_to_remove.append((i,j))

        if len(sweetrolls_to_remove) > 0:
            grid = remove_sweetrolls(grid, sweetrolls_to_remove)
            res += len(sweetrolls_to_remove)

    print(res)


if __name__ == "__main__":
    main()

