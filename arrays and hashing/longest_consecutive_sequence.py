class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = sorted(set(nums))        
        sequences = []
        temp_arr = []
        print(nums)
        if len(nums):
            for i in range(nums[0],nums[len(nums)-1]+1):
                if i in nums:
                    temp_arr.append(i)
                elif len(temp_arr):
                    sequences.append(temp_arr)
                    temp_arr = []
            if len(temp_arr):
                sequences.append(temp_arr)
                temp_arr = []
            print(sequences)
            return sorted([len(i) for i in sequences])[len(sequences)-1]
        return 0        



nums = [9,1,4,7,3,-1,0,5,8,-1,6]

# Output: 4 
sol = Solution()
print(sol.longestConsecutive(nums))