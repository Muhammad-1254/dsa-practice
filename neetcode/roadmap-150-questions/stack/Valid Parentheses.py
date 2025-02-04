class Solution:
    def pop(self):
        return self.stack.pop()

    def push(self, item: str):
        self.stack.append(item)

    def isValid(self, s: str) -> bool:
        self.stack = []
        close_brackets = {"{": "}", "[": "]", "(": ")"}

        for bracket in s:
            if close_brackets.get(bracket):
                self.push(close_brackets.get(bracket))
            elif len(self.stack) and  bracket == self.pop():
                continue
            else:
                return False
        if  len(self.stack):
            return False
        return True

sol = Solution()

s = "[]"
print(f"expected: {True}, {sol.isValid(s)}")

s = "([{}])"
print(f"expected: {True}, {sol.isValid(s)}")

s = "[(])"
print(f"expected: {False}, {sol.isValid(s)}")


s = "["
print(f"expected: {False}, {sol.isValid(s)}")


s = "]"
print(f"expected: {False}, {sol.isValid(s)}")