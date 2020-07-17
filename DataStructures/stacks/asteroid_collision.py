#https://leetcode.com/problems/asteroid-collision/
# TC:O(N)
# SC:O(N)
class Solution:
    def helper_stack(self, asteroids):
        stack = list()
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0 and stack[-1] < -asteroid:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                elif stack[-1] == -asteroid:
                    stack.pop()
        return stack

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if not asteroids:
            return []

        return self.helper_stack(asteroids)
