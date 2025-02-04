class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        while i < len(nums):
            if i + 2 < len(nums) and nums[i] == nums[i + 2]:
                nums.pop(i+2)
            else:
                i += 1
        return len(nums)

sol = Solution()


nums = [0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3]
# Output: 7  nums = [0,0,1,1,2,3,3,_,_]

print(sol.removeDuplicates(nums))
print(nums)
