


def update_range_in_lite(range_lite:list[int], range_from_input:list[int], ranges_lite_new):
    # case 1:
    # lite :       =======================
    # input:              ---------
    if range_from_input[0] >= range_lite[0] and range_from_input[1] <= range_lite[1]:
        # do nothing, no need to update lite
        pass
    # case 2:
    # lite :       =======================
    # input:    -------------------------------
    if range_from_input[0] < range_lite[0] and range_from_input[1] > range_lite[1]:
        # append fixed range to range_new



def main():
    with open("input_day5.txt", "r") as f:
        chunk1 = f.read().strip().split("\n\n")[0].strip()
    all_num = [int(num)  for row in chunk1.split("\n") for num in row.split("-")]
    min_num = min(all_num)
    ranges = [[int(range_.split("-")[0])-min_num, int(range_.split("-")[1])-min_num] for range_ in chunk1.split("\n")]

    ranges_lite = [ranges[0]]
    for range_ in ranges[1:]:
        # Compare with ranges in ranges_lite
        ranges_lite_new = []
        for i in range(len(ranges_lite)):
            update_range_in_lite(ranges_lite[i], range_, ranges_lite_new)
        
        # internal compare of ranges_lite: no overlap
        # re arrange order of ranges_lite: small to big


    



if __name__ == "__main__":
     main()

