class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            curr = asteroids[i]
            while stack and curr < 0 and stack[-1] > 0:
                diff = curr + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    curr = 0
                else:
                    curr = 0
                    stack.pop()
            if curr:
                stack.append(curr)


        return stack

        