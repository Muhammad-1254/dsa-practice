class Solution:
    def maxAreaBruteForce(self, heights: list[int]) -> int:
        results = []
        for i in range(0, len(heights) - 1):
            for j in range(i + 1, len(heights)):
                water_bet = min(heights[i], heights[j]) * (j - i)
                results.append(water_bet)

        return max(results)

    def maxArea(self, heights: list[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_bet = 0

        while left < right:
            water_bet = min(heights[left], heights[right]) * (right - left)
            max_bet = max(water_bet, max_bet)
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_bet


heights = [1, 7, 2, 5, 4, 7, 3, 6]
heights = [1, 7, 2, 5, 12, 3, 500, 500, 7, 8, 4, 7, 3, 6]

sol = Solution()
print(sol.maxArea(heights))
# sorted [1, 2, 3, 4, 5, 6, 7, 7]
# Output: 36
