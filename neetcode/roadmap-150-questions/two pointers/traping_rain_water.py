class Solution:
    def trap(self, height: list[int]) -> int:
        if not height or len(height) < 3:
            return 0  # No water can be trapped if there are fewer than 3 bars
        
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        trapped_water = 0

        while left < right:
            if height[left] < height[right]:
                # Process the left pointer
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    trapped_water += left_max - height[left]
                left += 1
            else:
                # Process the right pointer
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    trapped_water += right_max - height[right]
                right -= 1

        return trapped_water


height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
sol = Solution()
print(sol.trap(height))


# Output: 9
