import copy
from tqdm import tqdm
import unittest




class TestPart1FlattenList(unittest.TestCase):
    
    def test_flatten_list_with_simple(self):
        # Test with even numbers
        path = "simple.txt"
        blink = 1
        expected_output = [1, 2024, 1, 0, 9, 9, 2021976]
        self.assertEqual(part_1_flatten_list(path, blink), expected_output)

    def test_flatten_list_with_sample(self):
        # Test with even numbers
        path = "sample.txt"
        blink = 6
        expected_output = [2097446912, 14168, 4048, 2, 0, 2, 4, 40, 48, 2024, 40, 48, 80, 96, 2, 8, 6, 7, 6, 0, 3, 2]
        self.assertEqual(part_1_flatten_list(path, blink), expected_output)

    def test_flatten_list_with_sample2(self):
        # Test with even numbers
        path = "sample.txt"
        blink = 25
        expected_output = 55312
        self.assertEqual(len(part_1_flatten_list(path, blink)), expected_output)







def part_1_deprecated(path:str, blink:int):
    """Result incorrect, root cause: indexing"""
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
                data[i] = v * 2024
            print(data)



def flatten_list(nested_list:list) -> list:
    """Flatten a list containing integers and lists of integers."""
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))  # Recursively flatten the sublist
        else:
            flat_list.append(item)  # Append the integer
    return flat_list



def part_1_flatten_list(path:str, blink:int):
    with open(path, "r") as f:
        data =  [int(num) for num in f.read().strip().split(" ")]
    
    # test purpose
    print(data)

    for _ in tqdm(range(blink)):
        for i,v in enumerate(data):
            if v==0:
                data[i] = 1
            elif len(str(v)) % 2 == 0:
                data[i] = [int( str(v)[:int(len(str(v))/2)] ),   int(str(v)[int(len(str(v))/2):])]
            else:
                data[i] = v * 2024
        # Flatten list before next blink
        data = flatten_list(data)
        #print(data)
    print(len(data))
    return data



def part_1_linked_list(path:str, blink:int):
    pass



def main():
    path = "sample.txt"
    blink = 6
    part_1_flatten_list(path, blink)



if __name__ == "__main__":
    unittest.main()

