import copy



def part_1_deprecated(path:str, blink:int):
    with open(path, "r") as f:
        data =  [int(num) for num in f.read().strip().split(" ")]

    for _ in range(blink):
        tmp = copy.deepcopy(data)
        print(f"blink is {_}")
        for i,v in enumerate(tmp):
            print(f"i,v {i, v}")
            if v == 0:
                print("if")
                data[i] = 1
            elif len(str(v)) % 2 == 0:
                print("elif")
                data = data[:i] + [int( str(v)[:int(len(str(v))/2)] )] + [int(str(v)[int(len(str(v))/2):])] + data[i+1:]
            else:
                print("else")
                data[i] = v * 1024
            print(data)

    breakpoint()




def main():
    path = "test.txt"
    blink = 2
    part_1(path, blink)



if __name__ == "__main__":
    main()

