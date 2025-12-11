



def is_invalid_id(num:int) -> bool:
    if len(str(num)) % 2 == 1:
        return False
    left = str(num)[ : int(len(str(num))/2)]
    right = str(num)[int(len(str(num))/2) : ]
    return left==right



def main():
    with open("day2_input.txt", "r") as f:
        ranges = f.read().strip().split(",")
    
    res = 0
    for range_ in ranges:
        print(f"checking range {range_}")
        start = int(range_.split("-")[0])
        end = int(range_.split("-")[1])

        # if both range start and range end have odd digits
        # impossible to find invalid ID
        if len(str(start))%2==1 and len(str(end))%2==1:
            continue

        for i in range(start, end+1):
            if is_invalid_id(i):
                print(f"    Found {i}")
                res += i

    print(res)


if __name__ == "__main__":
    main()


