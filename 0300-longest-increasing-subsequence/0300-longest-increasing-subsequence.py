class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def bs(origin, num):
            l = 0
            r = len(origin) -1

            while l <= r:
                m = (l+r) // 2

                if origin[m] == num:
                    return m
                elif origin[m] < num:
                    l = m +1
                else:
                    r = m -1
            return l
        
        origin = []
        for num in nums:
            if len(origin) == 0 or origin[-1] < num:
                origin.append(num)
            else:
                index = bs(origin, num)
                origin[index] = num
        return len(origin)


        



