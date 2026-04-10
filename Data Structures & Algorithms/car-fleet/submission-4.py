class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        for i in range(len(position)):
            pos_speed.append((position[i], speed[i]))
        
        pos_speed.sort(key=lambda x: x[0])
        print(pos_speed)
        num_fleets = 1
        curr_val = -1
        for i in range(len(pos_speed) - 1, -1, -1):
            eta = ((target - pos_speed[i][0]) / pos_speed[i][1])
            if curr_val > -1 and eta > curr_val:
                num_fleets += 1
                curr_val = eta
            elif curr_val == -1:
                curr_val = eta
        
        return num_fleets
        