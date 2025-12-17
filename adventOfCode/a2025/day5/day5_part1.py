

def main():
    with open("input_day5.txt", "r") as f:
        input_ = f.read()
    ranges = input_.strip().split("\n\n")[0].split("\n")
    ingredients = input_.strip().split("\n\n")[1].split("\n")

    res = 0

    for ingredient in ingredients:
        for range_ in ranges:
            left = int(range_.split("-")[0])
            right = int(range_.split("-")[1])
            if int(ingredient) >= left and int(ingredient) <= right:
                res += 1
                break # jump to next ingredient
    
    print(res)



if __name__ == "__main__":
     main()

