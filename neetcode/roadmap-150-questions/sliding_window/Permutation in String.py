class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, 0
        s1_ = list(s1)
        while left < len(s2):
            if s2[left] in s1_:
                if left + len(s1) > len(s2):
                    return False
                for right in range(left, left + len(s1)):
                    if s2[right] in s1_:
                        s1_.remove(s2[right])
                    else:
                        s1_ = list(s1)
                        break
            if not len(s1_):
                return True
            left += 1

        return False


sol = Solution()
s1 = "abc"
s2 = "lecaabee"
print(f"expected: {False} {sol.checkInclusion(s1,s2)}")
# Output: false

s1 = "abc"
s2 = "lecabee"
print(f"expected: {True} {sol.checkInclusion(s1,s2)}")

# Output: true

s1 = "xyz"
s2 = "yxzabc"
print(f"expected: {True} {sol.checkInclusion(s1,s2)}")
# Output: true

s1 = "abcd"
s2 = "efghijklmnop"
print(f"expected: {False} {sol.checkInclusion(s1,s2)}")
# Output: false

s1 = "aabb"
s2 = "babbaa"
print(f"expected: {True} {sol.checkInclusion(s1,s2)}")

# Output: true

s1 = "hello"
s2 = "ooolleoooleh"
print(f"expected: {False} {sol.checkInclusion(s1,s2)}")

# Output: false

s1 = "abcd"
s2 = "dcbaefg"
print(f"expected: {True} {sol.checkInclusion(s1,s2)}")
# Output: true
