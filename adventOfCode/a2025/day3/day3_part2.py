

def main():
    with open("input_day3.txt", "r") as f:
        batteries = f.read().strip().split("\n")
    
    res = 0

    length_battery = len(batteries[0])


    for bank in batteries:
        # As we can turn on 12 battery, to find the first battery
        # to turn on, we must reserve at least 11 bateries.
        # This number decrement with each iteration
        int_reserve = 11
        str_joltage = ""

        # Find joltage of the bank
        for _ in range(12):
            if int_reserve != 0:
                left = max([int(c) for c in list(bank[:-1*int_reserve])])
            else:
                left = max([int(c) for c in list(bank)])
            str_joltage += str(left)
            bank = bank[bank.find(str(left))+1:]
            int_reserve -= 1

        print(str_joltage)
        res += int(str_joltage)
    
    print("--------")
    print(res)
        



if __name__ == "__main__":
    main()


