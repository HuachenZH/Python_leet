class Solution:
    def countLargestGroup(self, n: int) -> int:
        # create a dictionary, iterate from 1 to n
        # the key is digit sum
        # the value is numbers which gives the digit sum
        # then iterate through the values,
        # find who has biggest size and count how many are them
        hashmap = {} # key: digit sum. value: number from 1 to n
        for num in range(1, n+1):
            # get digit sum of num 
            # it will be a new key in hashmap
            digsum = sum(int(i) for i in [*str(num)])
            # if this key does not existe yet, initialize an empty list
            if not digsum in hashmap:
                hashmap[digsum] = []
            # if the key already existes
            hashmap[digsum].append(num)
        # print(hashmap)  # uncomment for debugging
        # count size
        list_size = []
        for v in hashmap.values():
            list_size.append(len(v))
        # print(list_size)  # uncomment for debugging
        return list_size.count(max(list_size))
epsi = Solution()
print(epsi.countLargestGroup(2))