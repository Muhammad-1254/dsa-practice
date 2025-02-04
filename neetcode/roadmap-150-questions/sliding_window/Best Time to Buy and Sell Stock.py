class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left, right = 0, 1
        max = 0
        while left < len(prices) - 1:
            if  right == len(prices) or prices[left] > prices[right]  :
                left += 1
                right = left + 1
                continue
            profit = prices[right] - prices[left]
            if profit > max:
                max = profit
            right += 1
        return max


prices = [10, 1, 5, 6, 7, 1]
# Output: 6
prices = [10,8,7,5,2]
# Output: 0

prices=[5,1,5,6,7,1,10]
# Output: 9

sol = Solution()
print(sol.maxProfit(prices))
