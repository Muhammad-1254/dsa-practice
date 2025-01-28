class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(0,len(nums)):
            prod = None
            for j in range(0, len(nums)):
                if i==j:
                    continue
                elif prod ==None:
                    prod = nums[j]
                else:
                    prod *=nums[j]
            result.append(prod)
        return result