class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        


        origin = []

        def bs(origin, target):
            l, r= 0, len(origin)-1

            while l<= r:

                mid = (l+r) // 2

                if origin[mid] == target:
                    return mid

                if origin[mid] < target:
                    l = mid +1
                else:
                    r = mid -1
            return l

        for num in nums:
            if len(origin) == 0 or origin[-1] < num:
                origin.append(num)
            else:
                index = bs(origin, num)
                origin[index] = num
        return len(origin)
