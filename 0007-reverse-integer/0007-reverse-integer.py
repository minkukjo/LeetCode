class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        ans = 0
        if x >0:
            ans = int(str(x)[::-1])
        else:
            ans = int(str(x)[1:][::-1]) * -1

        if -2 **31 < ans < 2**31:
            return ans

        return 0