class Solution:
    [5, 9, 1]
    def jump(self, nums: List[int]) -> int:
        pos = 0
        jumps = 0
        while pos < len(nums) - 1:
            if pos + nums[pos] >= len(nums) - 1:
                pos += nums[pos]
            else:
                max_dist = 0
                max_pos = pos
                for i in range(pos + 1, pos + nums[pos] + 1):
                    if i < len(nums) and i + nums[i] > max_dist:
                        max_dist = i + nums[i]
                        max_pos = i

                if max_dist == 0:
                    return False
                pos = max_pos

            jumps += 1
        
        return jumps

        