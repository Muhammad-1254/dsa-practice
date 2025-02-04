class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right =0
        max_len = 0
        while right<len(s):
            char_count = dict()
            # counts letters present in window
            for i in range(left,right+1):
                if s[i] in char_count:
                    char_count[s[i]]+=1
                else:
                    char_count[s[i]]=1

            window_len = len(s[left:right+1])
            t = window_len - char_count[max(char_count,key=char_count.get)]
            if t<=k :
                max_len = max(window_len,max_len)
            else: left+=1
            right+=1
        return max_len
sol =Solution() 


s="AABABBA"
k=1
# Output: 4
print(sol.characterReplacement(s,k))


s = "XYYX"
k = 2
# Output: 4
print(sol.characterReplacement(s,k))

s ="ABABBA"
k=2
# Output: 5
print(sol.characterReplacement(s,k))

s = "AAABABB"
k = 1
# Output: 5
print(sol.characterReplacement(s,k))
