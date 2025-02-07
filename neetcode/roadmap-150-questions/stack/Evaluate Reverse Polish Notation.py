class Solution:

    def evalRPN(self, tokens: list[str]) -> int:
        operators = {"-": "-", "+": "+", "/": "/", "*": "*"}
        stack = []
        exp = None
        for i in tokens:
            if i in operators:
                operator = operators.get(i)
                b,a = stack.pop(), stack.pop()
                if operator == "+":
                    exp = a + b
                elif operator == "-":
                    exp = a - b
                elif operator == "*":
                    exp = a * b
                else:
                    exp = int(a / b)
                stack.append(exp)
            else:
                stack.append(int(i))
        return stack[0]    


sol = Solution()

tokens = ["1", "2", "+", "3", "*", "4", "-"]
# Output: 5
# Explanation: ((1 + 2) * 3) - 4 = 5

print(f"exptecd: {5}, {sol.evalRPN(tokens)}")

tokens=["18"]
# Output: 18

print(f"exptecd: {18}, {sol.evalRPN(tokens)}")



tokens=["3", "2",'/']
# Output: 1

print(f"exptecd: {18}, {sol.evalRPN(tokens)}")

