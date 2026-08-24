class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Case 1: stack empty, curr > 0
        # Case 2: stack empty, curr < 0
        # Case 3: stack not empty, no collision
        # Case 4: Stack not empty, collision, curr destroyed
        # Case 5: stack not empty, collision, stack[-1] destroyed, while
        # Case 6: stack not empty, collision, curr and stack[-1] both destroyed
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

        