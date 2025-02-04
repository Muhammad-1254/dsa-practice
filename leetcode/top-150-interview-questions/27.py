class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i=0
        while i< len(nums):
            if nums[i] == val:
                nums.pop(i)
            else: i+=1
            
sol = Solution()


nums = [0,1,2,2,3,0,4,2]
val = 2
sol.removeElement(nums, val)
print(nums)
# Output: 5, nums = [0,1,4,0,3,_,_,_]
