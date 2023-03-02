class Solution:
    # same approach for every version. Consists of 3 parts:
    # 1 list to int
    # 2 sum
    # 3 int to list


    # ver alpha
    # list to int  and  int to list,  i use pure math approach, without str
    # runtime 7151 ms 5%
    # memory 15 MB 61.63%
    def addToArrayFormAlpha(self, num: list[int], k: int) -> list[int]:
        # turn the list num to a true number
        k0 = 0
        for i in range(len(num)):
            # print(len(num)-i-1)
            # print(num[i])
            # print()
            k0 += num[i] * 10**(len(num)-i-1)
        print(k0)

        # add the two number
        summ = k0 + k
        print(summ)

        # split digits, add to a list
        res = []
        while summ > 0:
            res.insert(0, summ % 10)
            summ //= 10
        return res

    # ver beta
    # use str for both int to list  and list to int
    # a bit verbose for the third part, int to list
    # runtime 324 ms 48.50%
    # memory 15 MB 61.63%
    def addToArrayFormBeta(self, num: list[int], k: int) -> list[int]:
        # num to true number
        k0 = ""
        k0 = int("".join(str(digit) for digit in num))
        # print(k0)
        summ = k0 + k

        # split the string and convert to int, add to list
        res = [] 
        for i in [*str(summ)]:
            res.append(int(i))
        return res

    # ver gamma
    # third part int to list less verbose
    # use map()
    # runtime 308 ms 64.36%
    # memory 15 MB 61.63%
    def addToArrayFormGamma(self, num: list[int], k: int) -> list[int]:
        # num to true number
        k0 = ""
        k0 = int("".join(str(digit) for digit in num))
        # print(k0)
        summ = k0 + k

        # split the string and convert to int, add to list
        return list(map(int, [*str(summ)]))

    # ver delta
    # third part int to list
    # use list comprehension
    # runtime 313 ms 60.18%
    # memory 15.2 MB 32.88%
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        # num to true number
        k0 = ""
        k0 = int("".join(str(digit) for digit in num))
        # print(k0)
        summ = k0 + k

        # split the string and convert to int, add to list
        return [int(i) for i in [*str(summ)]]

epsi = Solution()
print(epsi.addToArrayForm([2,1,5], 806))
