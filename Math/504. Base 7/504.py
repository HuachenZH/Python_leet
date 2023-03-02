class Solution:
    # runtime 32 ms 68.20%
    # memory 13.8 MB 50.82%
    def convertToBase7(self, num: int) -> str:
        listres = []
        if num == 0:
            return "0"
        
        isNegatif = False
        if num < 0:
            num *= -1
            isNegatif = True
        
        # ref 1837 sum of digits in base k
        while num > 0:
            listres.append(num%7)
            num = num //7
        # print(listres) 
        # for exemple, is listres is [2, 1]
        #                             ^      unit's digit
        #                                ^   ten's digit
        res = ""
        for digit in listres[::-1]:
            res += str(digit)
        if isNegatif:
            res = "-" + res
        return res
epsi = Solution()
print(epsi.convertToBase7(-100))

# ---------------------------------------------------
# for further use
# convert num to base k
def convertToBasek(num: int, k: int) -> str:
    """
    num : the number to be converted
    k : to be converted in base k

    return a string
    """
    if num == 0:
        return "0"

    isNegatif = False
    if num < 0:
        num *= -1
        isNegatif = True
    
    listres = []
    while num > 0:
            listres.append(num%k)
            num = num //k

    # concat the result
    res = ""
    for digit in listres[::-1]:
        res += str(digit)
    if isNegatif:
        res = "-" + res
    return res
print(convertToBasek(-100,7))
