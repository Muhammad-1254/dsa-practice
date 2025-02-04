class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            if right-left+1>max_len:
                max_len = right-left+1
        return max_len


sol = Solution()
s = "zxyzxyz"  # 3
s = "xxxx"  # 1
s = 'abcdcbbccc'
print(sol.lengthOfLongestSubstring(s))
