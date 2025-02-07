class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def backtrack(open, close):
            if open==close==n:
                res.append("".join(stack))
                return
            if open<n:
                stack.append("(")
                backtrack(open+1,close)
                stack.pop()
            if close<open:
                stack.append(")")
                backtrack(open,close+1)
                stack.pop()
        backtrack(0,0)
        return res
sol = Solution()

n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
print(sol.generateParenthesis(n))

n = 1
# Output: ["()"]
print(sol.generateParenthesis(n))
