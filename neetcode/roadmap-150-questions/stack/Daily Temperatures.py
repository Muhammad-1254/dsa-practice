class Solution:
    def dailyTemperaturesBruteForce(self, temperatures: list[int]) -> list[int]:
        res = []
        for i in  range(len(temperatures)):
            is_found=False
            for j in  range(i+1, len(temperatures)):
                if temperatures[i] <temperatures[j]:
                    res.append(abs(j-i))
                    is_found=True
                    break
            if not is_found:
                res.append(0)
        return res
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        res = [0]*len(temperatures)
        
        for i in range(len(temperatures)):
            j = len(stack) -1
            while j>=0:
                if stack[j]['value']< temperatures[i]:
                    item = stack.pop()
                    res[item['index']] = abs(i-item['index'])
                    j-=1
                    continue
                break
            stack.append({"index":i,"value":temperatures[i]})
        return res

sol = Solution()
temperatures = [30,38,30,36,35,40,28]
# Output: [1,4,1,2,1,0,0]
print(f'{[1,4,1,2,1,0,0]==sol.dailyTemperatures(temperatures)}')


temperatures = [22,21,20]
# Output: [0,0,0]

print(f'{[0,0,0]==sol.dailyTemperatures(temperatures)}')
