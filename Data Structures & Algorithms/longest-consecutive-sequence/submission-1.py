class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        discovered_set = set()
        for num in num_set:
            if num in discovered_set:
                continue
            if num - 1 not in num_set:
                discovered_set.add(num)
                curr = 0
                num_val = num
                while num_val in num_set:
                    discovered_set.add(num_val)
                    curr += 1
                    num_val += 1
                longest = max(longest, (num_val - num))
        
        return longest
                

