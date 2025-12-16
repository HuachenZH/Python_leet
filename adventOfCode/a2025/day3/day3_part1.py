

def main():
    with open("input_day3.txt", "r") as f:
        batteries = f.read().strip().split("\n")
    
    res = 0

    for bank in batteries:
        left = max([int(c) for c in list(bank[:-1])])
        bank = bank[bank.find(str(left))+1:]
        right = max([int(c) for c in list(bank)])
        tmp = int(str(left)+str(right))
        res += tmp
    
    print(res)
        



if __name__ == "__main__":
    main()


