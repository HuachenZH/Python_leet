def preprocess_grid(grid:list[str]) -> list[str]:
    # Preprocess grid, add four edges of "...."
    grid = ["."+row+"." for row in grid]
    grid = [len(grid[0]) * "."] + grid + [len(grid[0]) * "."]
    return grid




def count_adj_sweetrolls(grid:list[str], irow:int, icol:int) -> int:
    grid[irow][icol]



def main():
    with open("input_day4_small.txt", "r") as f:
        grid = f.read().strip().split("\n")
    
    print("[*] before preprocessing, grid is:")
    print("\n".join(grid))
    grid = preprocess_grid(grid)
    print("[*] after preprocessing, grid is:")
    print("\n".join(grid))

    res = 0
    for i, row in enumerate(grid):
        for j in range(len(row)):
            if row[j] == "@":
                count_adj_sweetrolls(grid, i, j)




if __name__ == "__main__":
    main()

