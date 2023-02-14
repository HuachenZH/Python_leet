class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        ans = []
        for i in range(num_people):
            ans.append(0)
        remain = candies
        candiesToGive = 1
        indexPeople = 0
        while remain >= candiesToGive:           
            ans[indexPeople] += candiesToGive
            candiesToGive -=- 1
            indexPeople -=- 1
            if indexPeople > num_people-1:
                indexPeople = 0
            remain -= candiesToGive
        ans[indexPeople] += remain
        return ans
