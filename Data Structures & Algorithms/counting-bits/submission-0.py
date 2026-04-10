class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            x = i
            count = 0
            while x > 0:
                if x & 1 == 1:
                    count += 1
                x = x >> 1
            result.append(count)

        return result
        