class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = list(zip(position,speed)) 
        cars.sort()
        stack = []
        for i in range(len(cars)-1,-1,-1):
            speed_to_target = (target-cars[i][0])/cars[i][1]
            if len(stack):
                if stack[-1]>=speed_to_target:
                    continue
            stack.append(speed_to_target)
        return len(stack)

sol = Solution()


target = 10
position = [1, 4]
speed = [3, 2]

print(f"expected: {1}, {sol.carFleet(target,position,speed)}")

target = 10
position = [4, 1, 0, 7]
speed = [2, 2, 1, 1]
print(f"expected: {3}, {sol.carFleet(target,position,speed)}")
