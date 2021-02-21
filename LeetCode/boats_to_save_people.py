class Solution:
    def numRescueBoats(self, people, limit):
        boats = 0
        while len(people) > 0:
            people.sort()
            maxm = max(people)
            people.remove(maxm)
            remaining_space = limit-maxm
            if remaining_space > 0:
                for p in people:
                    if p <= remaining_space:
                        people.remove(p)
                        break
            boats+=1
        return boats
        
s = Solution()
print(s.numRescueBoats([3,8,7,1,4], 9))