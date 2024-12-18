import copy
from tqdm import tqdm
import unittest




class TestPart1FlattenList(unittest.TestCase):
    
    def test_maphash_with_simple(self):
        # Test with even numbers
        path = "simple.txt"
        blink = 1
        expected_output = len([1, 2024, 1, 0, 9, 9, 2021976])
        self.assertEqual(part_2_maphash(path, blink), expected_output)

    def test_maphash_with_sample(self):
        # Test with even numbers
        path = "sample.txt"
        blink = 6
        expected_output = len([2097446912, 14168, 4048, 2, 0, 2, 4, 40, 48, 2024, 40, 48, 80, 96, 2, 8, 6, 7, 6, 0, 3, 2])
        self.assertEqual(part_2_maphash(path, blink), expected_output)

    def test_maphash_with_sample2(self):
        # Test with even numbers
        path = "sample.txt"
        blink = 25
        expected_output = 55312
        self.assertEqual(part_2_maphash(path, blink), expected_output)

    def test_maphash_with_data(self):
        # Test with even numbers
        path = "data.txt"
        blink = 25
        expected_output = 194557
        self.assertEqual(part_2_maphash(path, blink), expected_output)





def part_2_maphash(path:str, blink:int):
    with open(path, "r") as f:
        data = [int(num) for num in f.read().strip().split()]
    dict_occur = {}
    for num in data:
        if num in dict_occur:
            dict_occur[num] += 1
        else:
            dict_occur[num] = 1
    
    for _ in range(blink):
        dict_tmp = copy.deepcopy(dict_occur)
        for key in list(dict_occur.keys()):
            if key == 0:
                #dict_occur[1] = dict_occur[key]
                dict_occur[1] = dict_occur[1]+dict_occur[key] if 1 in dict_occur else dict_occur[key]
                del dict_occur[key]
            elif len(str(key))%2==0:
                new_key_1 = int(str(key)[:int(len(str(key))/2)])
                new_key_2 = int(str(key)[int(len(str(key))/2):])
                dict_occur[new_key_1] = dict_occur[new_key_1]+dict_occur[key] if new_key_1 in dict_occur else dict_occur[key]
                dict_occur[new_key_2] = dict_occur[new_key_2]+dict_occur[key] if new_key_2 in dict_occur else dict_occur[key]
                del dict_occur[key]
            else:
                dict_occur[key*2024] = dict_occur[key*2024]+dict_occur[key] if key*2024 in dict_occur else dict_occur[key]
                del dict_occur[key]
        #breakpoint()

    res = len(list(dict_occur.values()))
    print(res)
    return res






def main():
    path = "sample.txt"
    blink = 6
    part_2_maphash(path, blink)



if __name__ == "__main__":
    #unittest.main()
    main()