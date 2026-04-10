from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        results = c.most_common(k)
        return [num for num, _ in results]
        