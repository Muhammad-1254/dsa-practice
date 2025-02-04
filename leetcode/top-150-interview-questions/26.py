class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        while i < len(nums):

            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)

sol = Solution()

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


print(sol.removeDuplicates(nums))
print(nums)


# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
