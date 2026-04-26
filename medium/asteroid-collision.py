class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #monotonic stack
        stack = []

        #while the sign is different: peek top, if top > curr then curr loses, otherwise keep going
        #answer should just be the stack at the end

        for num in asteroids:
            destroyed = False
            while stack and stack[-1] > 0 and num < 0:
                if stack[-1] < abs(num):
                    stack.pop()
                    continue
                elif stack[-1] == abs(num):
                    stack.pop()
                    destroyed = True
                else:
                    destroyed = True
                break
            
            if not destroyed:
                stack.append(num)

        return stack