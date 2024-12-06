class Solution:
    def reverseBits(self, n: int) -> int:
        t = bin(n)[2::]
        
        while len(t) < 32:
            t = "0" + t


        return int(t[::-1],2)