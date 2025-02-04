class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        m= dict()
        for item in nums:
            if m.get(item):
                m[item] +=1
            else:
                m[item] =1
        return max(m,key=m.get)
        

sol = Solution ()


nums = [2,2,1,1,1,2,2]
# Output: 2

print(sol.majorityElement(nums))
