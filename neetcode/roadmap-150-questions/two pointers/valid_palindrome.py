class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        print(s)
        if len(s)==0:
            return True
        half_len = len(s)//2 
        for i in range(half_len+1):
            if s[i]!=s[len(s)-1-i]:
                print(f"{ s[i]}!={s[len(s)-1-i]}")
                return False
        return True



s = 'abba'
s=' '
s="tab a cat"
s = "Was it a car or a cat I saw?" 
s='0P'

sol = Solution()
print(
sol.isPalindrome(s)
)

# Output: true
# wasitacaroracatisaw


