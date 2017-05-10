"""
Solution:
1. Convert int to bin, we will get s = '0b0101'
2. Set s to '0101' by assigning s = s[2:]
3. To make it 32 bits, zfill(32), which will fill s with 0s so that it becomes 32 bits
4. return s[::-1]
"""


class Solution:
    # @param n, an integer
    # @return an integer

    def reverseBits(self, n):
        s = bin(n)
        s = s[2:].zfill(32)
        return int(s[::-1], 2)
