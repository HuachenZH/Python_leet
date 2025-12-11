# in the input ranges, the largest number has 10 digits


def get_divisors_without_one_and_self(n:int):
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            yield i


def num_has_same_digits(num:int) -> bool:
    standard = str(num)[0] * len(str(num))
    return int(standard) == num



def is_invalid_id(num:int) -> bool:
    res = False
    divisors = get_divisors_without_one_and_self(len(str(num)))
    #for divisor in divisors:
    #    notch = 10 ** divisor
    #    counter = 1
    #    prev = (num % (notch**counter)) / (notch**(counter-1))
    #    for _ in range(int(len(str(num)) / divisor)):
    #        counter += 1
    #        curr = ( (num - num%(notch**(counter-1))) % (notch**counter)) / (notch**(counter-1))
    #        if num == 1188511885:
    #            breakpoint()
    #        if curr != prev:
    #            continue # jump to next divisor but not next _
    #        prev = curr
    #    return True
    #raise RuntimeError("Shouldn't hit this line. All iteration finished but True isn't returned")

    for divisor in divisors:
        # num=1188511885, divisor=2
        tmp = [str(num)[i*divisor : (i+1)*divisor] for i in range(int(len(str(num)) / divisor))]
        # check all elements are the same
        iterator = iter(tmp)
        first = next(iterator)
        res = all(first == x for x in iterator)
        #_if num ==824824824: 
        #_    breakpoint()
        if res:
            return True
    return res




def main():
    with open("day2_input.txt", "r") as f:
        ranges = f.read().strip().split(",")

    res = 0
    for range_ in ranges:
        for num in range(int(range_.split("-")[0]), int(range_.split("-")[1])+1) :
            if len(str(num)) == 1:
                continue
            if num_has_same_digits(num):
                res += num
                print(num)
                continue

            #_if num ==824824824: 
            #_    breakpoint()
            # number of odd digits (and not 9 digits), only possible invid ID is a number that all digits are the same
            # such as 111, 999
            if len(str(num)) % 2 == 1 and len(str(num))!=9: 
                continue
            # number of two digits, 12, 28 etc
            elif len(str(num)) == 2:
                continue
            # number of even digits, such as 1234, 12
            else:
                if is_invalid_id(num):
                    res += num
                    print(num)

    print("--")
    print(res)



if __name__ == "__main__":
    main()


