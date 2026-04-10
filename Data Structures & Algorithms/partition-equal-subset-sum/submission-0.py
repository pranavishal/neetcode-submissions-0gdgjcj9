class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # We know that the entire array must be partitioned into 2 sets, and the sums of
        # Each set must be equal. Thus, each set must sum to sum(nums) / 2.
        # This requires sum(nums) % 2 == 0. If this was odd, no way to divide by two
        # into 2 partitions! This is the first check.
        # Assume now it is even
        # As you iterate through nums, store all possible sum values in a set. For each num,
        # add it to all elements in the set and add it to the set. 
        # Once done, return if sum(nums) / 2 is in the set. Because this must have came from
        # some strict subset from all nums since all nums sum to sum(nums) and not sum(nums) / 2
        partition_sum = (sum(nums)) 
        if partition_sum % 2 == 1:
            return False
        
        partition_sum /= 2
        sum_set = {nums[0]}
        for i in range(1, len(nums)):
            for val in list(sum_set):
                sum_set.add(val + nums[i])
        
        return partition_sum in sum_set
            

        