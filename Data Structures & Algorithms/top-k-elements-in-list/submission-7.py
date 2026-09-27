from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = defaultdict(int)
        for num in nums:
            num_map[num] += 1
        
        freq_list = [[] for _ in range(len(nums))]
        for key, val in num_map.items():
            freq_list[val - 1].append(key)

        returnVal = []
        for i in range(len(nums) - 1, -1, -1):
            for x in freq_list[i]:
                returnVal.append(x)
                if len(returnVal) == k:
                    return returnVal
        
        return returnVal
