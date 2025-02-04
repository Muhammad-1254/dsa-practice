class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        if len(s) < len(t):
            return ""
        min_sub = ""
        left = 0
        right = 0

        def count_str(s: str, d, method="inc"):
            if method=='inc':
                d = {key: 0 for key in d}
            for l in s:
                if l in d:
                    if method == "inc":
                        d[l] += 1
                    else:
                        d[l] -= 1
            return d
            

        t_count = Counter(t)
        c_count = {key: 0 for key in t_count}

        def is_valid_counts() -> bool:
            for i in t_count:
                if t_count[i] > c_count[i]:
                    return False
            return True

        while left < len(s) - len(t) :
            if is_valid_counts():
                if s[left] in t:
                    c_count[s[left]]  -= 1
                temp = s[left : right + 1]
                if len(temp) < len(min_sub):
                    min_sub = temp
                left += 1
                
            else:
                while right < len(s):
                    if s[right] in t:
                        temp = s[left : right + 1]
                        c_count = count_str(temp, c_count)
                        if is_valid_counts():
                            if len(temp) < len(min_sub) or not len(min_sub):
                                min_sub = temp
                            break
                    right += 1

        return min_sub



sol = Solution()

s="aabbbcdd"
t="abcdd"

print(f'expected: {"abbbcdd"}: {sol.minWindow(s,t)}')


# s = "OUZODYXAZV"
# t = "XYZ"
# print(f'expected: {"YXAZ"}: {sol.minWindow(s,t)}')

# s = "xyz"
# t = "xyz"
# print(f'expected: {"xyz"}: {sol.minWindow(s,t)}')

# s = "x"
# t = "xy"
# print(f'expected: {""}: {sol.minWindow(s,t)}')


# s = "ADOBECODEBANC"
# t = "ABC"
# print(f'expected: {"BANC"}: {sol.minWindow(s, t)}')

# s = "AABZCBBANC"
# t = "ABC"
# print(f'expected: {"BANC"}: {sol.minWindow(s, t)}')

# s = "AA"
# t = "AAA"
# print(f'expected: {""}: {sol.minWindow(s, t)}')

# s = "ABC"
# t = "CBA"
# print(f'expected: {"ABC"}: {sol.minWindow(s, t)}')

# s = "BACAD"
# t = "AAD"
# print(f'expected: {"ACAD"}: {sol.minWindow(s, t)}')


# s = "AAABBC"
# t = "ABC"
# print(f'expected: {"ABBC"}: {sol.minWindow(s, t)}')
