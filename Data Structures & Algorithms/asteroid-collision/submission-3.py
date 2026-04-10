class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        collision_stack = []
        for asteroid in asteroids:
            if asteroid < 0:
                while collision_stack and collision_stack[-1] > 0 and abs(collision_stack[-1]) < abs(asteroid):
                    collision_stack.pop()
                if len(collision_stack) == 0 or collision_stack[-1] < 0:
                    collision_stack.append(asteroid)
                elif abs(collision_stack[-1]) == abs(asteroid):
                    collision_stack.pop()
            else:
                collision_stack.append(asteroid)
        
        return collision_stack

            


        