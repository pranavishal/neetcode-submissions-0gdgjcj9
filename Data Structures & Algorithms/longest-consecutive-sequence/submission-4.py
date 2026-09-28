class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        for num in nums:
            if num - 1 not in num_set:
                curr_len = 1
                curr_num = num
                while curr_num + 1 in num_set:
                    curr_len += 1
                    curr_num += 1
                
                longest = max(longest, curr_len)
        
        return longest
        