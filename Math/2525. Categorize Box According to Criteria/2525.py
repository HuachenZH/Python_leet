class Solution:
    # runtime 35 ms 32.67%
    # memory 13.9 MB 73.57%
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        # is bulky or not ?
        is_bulkey = False
        if (length>=10000 or width>=10000 or height>=10000) or length*width*height>=10**9:
            is_bulkey = True
        
        # is heavy or not ?
        is_heavy = False
        if mass >= 100:
            is_heavy = True
        
        # return category
        if is_bulkey and is_heavy:
            return "Both"
        if is_bulkey == False and is_heavy == False:
            return "Neither"
        if is_bulkey == True and is_heavy == False:
            return "Bulky"
        if is_bulkey == False and is_heavy == True:
            return "Heavy"
        return -1
epsi = Solution()
print(epsi.categorizeBox(1000,35,700,300))
