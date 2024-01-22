class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)[2:].zfill(32)
        filtered = list(filter(lambda num: int(num) > 0, b))

        return len(filtered)