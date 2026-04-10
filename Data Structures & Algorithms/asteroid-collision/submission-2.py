class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        collision_stack = []
        for asteroid in asteroids:
            if asteroid < 0:
                should_append = True
                while collision_stack:
                    if collision_stack[-1] < 0:
                        should_append = True
                        break
                    elif abs(collision_stack[-1]) < abs(asteroid):
                        should_append = True
                        collision_stack.pop()
                    elif abs(collision_stack[-1]) == abs(asteroid):
                        should_append = False
                        collision_stack.pop()
                        break
                    else:
                        should_append = False
                        break
                if should_append:
                    collision_stack.append(asteroid)
            else:
                collision_stack.append(asteroid)
        
        return collision_stack

            


        