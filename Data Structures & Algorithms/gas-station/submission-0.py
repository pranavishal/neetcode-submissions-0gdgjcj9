class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net_array = [0] * len(gas)
        for i in range(len(gas)):
            net_array[i] = gas[i] - cost[i]
        
        if sum(net_array) < 0:
            return -1
        
        curr_sum = 0
        starting_index = 0
        for i in range(len(net_array)):
            if curr_sum < 0:
                starting_index = i
                curr_sum = 0
            
            curr_sum += net_array[i]

        return starting_index
                
