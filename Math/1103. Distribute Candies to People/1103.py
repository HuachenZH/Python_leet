class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        ans = []
        for i in range(num_people):
            ans.append(0)
        remain = candies
        candiesToGive = 1
        indexPeople = 0
        while remain >= candiesToGive:           
            print("indexPeople is %s" % indexPeople)
            print("candiesToGive is %s" % candiesToGive)
            ans[indexPeople] += candiesToGive
            remain -= candiesToGive
            candiesToGive -=- 1
            indexPeople -=- 1
            if indexPeople > num_people-1:
                indexPeople = 0
                print("indexPeople reset")
            print("remain is %s" % remain)
            print("answer is %s" % ans)
            print('\n')
        ans[indexPeople] += remain
        return ans

epsi = Solution()
print(epsi.distributeCandies(7,4))

# i think there might be pure maths approach.
# after half an hour playing with equations, i abandonned pure maths approach
# the algo is simple and stupid, however the performance is not bad
# runtime 81.93%
# memory 43.7%