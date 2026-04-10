class Solution:
    def reverseBits(self, n: int) -> int:
        new_num = 0
        for i in range(32):
            new_num = new_num << 1
            if n & 1 == 1:
                new_num += 1
            n = n >> 1

        return new_num

        