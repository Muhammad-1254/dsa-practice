class Solution:
    def threeSumBruteForce(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if i == j == k:
                        continue
                    elif (
                        nums[i] + nums[j] + nums[k] == 0
                        and sorted([nums[i], nums[j], nums[k]]) not in result
                    ):
                        result.append(sorted([nums[i], nums[j], nums[k]]))
        return result

    def threeSum2Pointer(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        results = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                
                if curr_sum > 0:
                    k -= 1
                elif curr_sum < 0:
                    j += 1
                if curr_sum == 0:
                    temp = sorted([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    if temp not in results:
                        results.append(temp)


        return results


nums = [0, 0, 0]
nums = [0, 1, 1]
nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()
print(sol.threeSum2Pointer(nums))


# n = set( [-1,0,1,2,-1,-4])
# print(list(n.copy()))
# Output: [[-1,-1,2],[-1,0,1]]
