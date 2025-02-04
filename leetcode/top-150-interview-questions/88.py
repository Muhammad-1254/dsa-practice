class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums2)):
            for j in range(len(nums1)):
                if nums1[j] == 0:
                    nums1[j] = nums2[i]
                    break
        nums1.sort()
                    


sol = Solution()


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
sol.merge(nums1,m,nums2,n)
print(nums1)