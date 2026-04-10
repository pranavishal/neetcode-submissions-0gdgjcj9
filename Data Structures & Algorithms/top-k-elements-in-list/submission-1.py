from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        output = []
        results = c.most_common(k)
        for result in results:
            output.append(result[0])
        return output
        